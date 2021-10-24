import glob
import io
import os

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

from nikola.plugin_categories import Task
from nikola import utils


class CopyNotebooks(Task):
    """Copy notebooks into pages."""

    name = "copy_notebooks"

    def set_site(self, site):
        self.site = site
        self.inject_dependency("render_posts", "copy_notebooks")
        self.site.register_shortcode("contents", self.handler)
        super(CopyNotebooks, self).set_site(site)

    def _get_kw(self):
        kw = {
            "filters": self.site.config["FILTERS"],
            "listing_folder": "listings",
            "notebooks_folder": self.site.config["NOTEBOOKS_FOLDER"],
            "pages_folder": "pages",
        }
        kw["notebooks"] = sorted(
            glob.glob(os.path.join(kw["notebooks_folder"], "*.ipynb"))
        )
        kw["scripts"] = sorted(glob.glob(os.path.join(kw["notebooks_folder"], "*.py")))
        return kw

    def gen_tasks(self):
        kw = self._get_kw()

        # copy scripts
        if not os.path.isdir(kw["listing_folder"]):
            os.mkdir(kw["listing_folder"])

        for i, src_file in enumerate(kw["scripts"]):
            dst_file = os.path.join(kw["listing_folder"], os.path.basename(src_file))
            task = {
                "basename": self.name,
                "name": dst_file,
                "file_dep": [src_file],
                "targets": [dst_file],
                "actions": [(copy_scripts, (src_file, dst_file))],
                "uptodate": [utils.config_changed(kw, "copy_notebooks")],
                "clean": True,
            }
            yield utils.apply_filters(task, kw["filters"])

        # copy notebooks
        if not os.path.isdir(kw["pages_folder"]):
            os.mkdir(kw["pages_folder"])

        for i, src_file in enumerate(kw["notebooks"]):
            dst_file = os.path.join(
                kw["pages_folder"], os.path.basename(src_file).replace("_", "-")
            )
            prev_nb, next_nb = None, None
            if i > 0:
                prev_nb = kw["notebooks"][i - 1]
            if i < len(kw["notebooks"]) - 1:
                next_nb = kw["notebooks"][i + 1]
            task = {
                "basename": self.name,
                "name": dst_file,
                "file_dep": [src_file],
                "targets": [dst_file],
                "actions": [
                    (
                        copy_notebooks,
                        (src_file, dst_file, prev_nb, next_nb, kw["notebooks_folder"]),
                    )
                ],
                "uptodate": [utils.config_changed(kw, "copy_notebooks")],
                "clean": True,
            }
            yield utils.apply_filters(task, kw["filters"])

    def handler(self, site=None, data=None, lang=None, post=None):
        kw = self._get_kw()

        output = []
        for nb_file in kw["notebooks"]:
            nb_link = get_nb_link(nb_file)
            nb_title = get_nb_title(nb_file)
            output.append(
                '<li><p><a href="{}">{}</a></p></li>'.format(nb_link, nb_title)
            )

        return "<ul>{}</ul>".format("".join(output)), kw["notebooks"]


def copy_scripts(src_file, dst_file):
    with open(src_file, "r") as f:
        content = f.read()

    with open(dst_file, "w") as f:
        f.write(content)


def copy_notebooks(src_file, dst_file, prev_nb, next_nb, notebook_folder):
    # navigation
    prev_link = get_nb_link(prev_nb) if prev_nb is not None else ""
    next_link = get_nb_link(next_nb) if next_nb is not None else ""
    prev_title = get_nb_title(prev_nb) if prev_nb is not None else ""
    next_title = get_nb_title(next_nb) if next_nb is not None else ""

    # read notebook
    with io.open(src_file, "r", encoding="utf8") as f:
        nb = nbformat.read(f, as_version=4)

    # execute notebook
    if "SVG" in os.environ:
        ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
        ep.preprocess(nb, {"metadata": {"path": notebook_folder}})

    # add title
    title = get_nb_link(src_file)
    for cell in nb.cells:
        if cell.cell_type == "markdown" and cell.source.startswith("#"):
            title = cell.source.splitlines()[0].lstrip("#").strip()
            cell.source = "\n".join(cell.source.splitlines()[1:])
            break
    nb.metadata.nikola = {"title": title}

    # add navigation
    nav_template = "<!-- NAVIGATION -->\n< [{}]({}) | [{}]({}) >"
    navigation = nav_template.format(prev_title, prev_link, next_title, next_link)
    navigation_cell = nbformat.v4.new_markdown_cell(
        navigation, metadata={"navigation": True}
    )
    del navigation_cell["id"]
    nb.cells.insert(0, navigation_cell)
    nb.cells.append(navigation_cell)

    # add colab cell
    colab_cell = nbformat.v4.new_markdown_cell(
        """<div class="admonition note">
          <span style="white-space: nowrap;">
            <a href="https://colab.research.google.com/github/fehiepsi/rethinking-numpyro/blob/master/notebooks/{}">
              <img alt="Open In Colab"
                src="https://colab.research.google.com/assets/colab-badge.svg"
                style="vertical-align:text-bottom">
            </a>
          </span>
        </div>""".format(
            src_file.split("/")[-1]
        )
    )
    del colab_cell["id"]
    nb.cells.insert(2, colab_cell)

    # reduce execution_count
    for cell in nb.cells:
        if "execution_count" in cell and cell.execution_count is not None:
            cell.execution_count -= 1

    # write notebook
    with io.open(dst_file, "w", encoding="utf8") as f:
        nbformat.write(nb, f)


def get_nb_link(nb_file):
    return os.path.basename(nb_file).replace("_", "-").replace(".ipynb", ".html")


def get_nb_title(nb_file):
    with io.open(nb_file, "r", encoding="utf8") as f:
        nb = nbformat.read(f, as_version=4)

    for cell in nb.cells:
        if cell.cell_type == "markdown" and cell.source.startswith("#"):
            return cell.source.lstrip("#").splitlines()[0].strip()

    return get_nb_link(nb_file)
