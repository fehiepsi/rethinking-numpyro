# Statistical Rethinking (2nd ed.) with NumPyro

**Status:** The codes here correspond to the book draft dated on 26 Sept 2019.

I am a fan of the book [*Statistical Rethinking*](https://xcelab.net/rm/statistical-rethinking/), so I port the codes of [its second edition](https://github.com/rmcelreath/statrethinking_winter2019#draft-chapters) to [NumPyro](https://github.com/pyro-ppl/numpyro). I hope that the book and this translation will be helpful not only for NumPyro/Pyro users but also for ones who are willing to do Bayesian statistics in Python.

## How to read the notebooks

+ Read on the site: https://fehiepsi.github.io/rethinking-numpyro/

+ Use GitHub's renderer: https://github.com/fehiepsi/rethinking-numpyro/tree/master/notebooks/

+ Use Jupyter's nbviewer: https://nbviewer.jupyter.org/github/fehiepsi/rethinking-numpyro/tree/master/notebooks/

## Installation

The following tools are used for some analysis and visualizations: [arviz](https://arviz-devs.github.io/arviz/) for [posteriors](https://en.wikipedia.org/wiki/Posterior_probability), [causalgraphicalmodels](https://github.com/ijmbarr/causalgraphicalmodels) for [causal graphs](https://en.wikipedia.org/wiki/Causal_graph), [ete3](http://etetoolkit.org/) for [phylogenetic trees](https://en.wikipedia.org/wiki/Phylogenetic_tree).

```sh
pip install numpyro causalgraphicalmodels ete3
pip install git+https://github.com/arviz-devs/arviz@refs/pull/852/head#egg=arviz
```

