{%- extends "classic/base.html.j2" -%}

{% block input_group -%}
{%- if cell.metadata.hide_input or nb.metadata.hide_input -%}
{%- else -%}
    {{ super() }}
{%- endif -%}
{% endblock input_group %}

{% block output_group -%}
{%- if cell.metadata.hide_output -%}
{%- else -%}
    {{ super() }}
{%- endif -%}
{% endblock output_group %}

{% block output_area_prompt %}
<div class="prompt output_prompt">
<span>
{%- if cell.execution_count is defined -%}
    Out[{{ cell.execution_count|replace(None, "&nbsp;") }}]:
{%- else -%}
    Out[&nbsp;]:
{%- endif -%}
</span>
</div>
{% endblock output_area_prompt %}

{% block markdowncell %}
{%- if cell.metadata.navigation -%}
    <div class="cell border-box-sizing text_cell rendered">
    <div class="inner_cell">
    <div class="text_cell_render border-box-sizing rendered_html">
    <div class="navigation">
    {{ cell.source  | markdown2html | strip_files_prefix }}
    </div>
    </div>
    </div>
    </div>
{%- else -%}
    {{ super() }}
{%- endif -%}
{%- endblock markdowncell %}
