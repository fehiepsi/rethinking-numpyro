<!--
.. title: Overview
.. slug: index
-->

I am a fan of the book [*Statistical Rethinking*](https://xcelab.net/rm/statistical-rethinking/), so I port the codes of [its second edition](https://github.com/rmcelreath/rethinking) to [NumPyro](https://github.com/pyro-ppl/numpyro). I hope that the book and this translation will be helpful not only for NumPyro/Pyro users but also for ones who are willing to do Bayesian statistics in Python.

## Contents

{{% contents %}}

## Installation

Data and notebooks can be found at [my github repository](https://github.com/fehiepsi/rethinking-numpyro).

The following tools are used for some analysis and visualizations: [arviz](https://arviz-devs.github.io/arviz/) for [posteriors](https://en.wikipedia.org/wiki/Posterior_probability), [causalgraphicalmodels](https://github.com/ijmbarr/causalgraphicalmodels) and [daft](https://docs.daft-pgm.org/en/latest/) for [causal graphs](https://en.wikipedia.org/wiki/Causal_graph), and (optional) [ete3](http://etetoolkit.org/) for [phylogenetic trees](https://en.wikipedia.org/wiki/Phylogenetic_tree).

```sh
pip install numpyro arviz causalgraphicalmodels daft
```
