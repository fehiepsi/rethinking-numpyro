<!--
.. title: Overview
.. slug: index
-->

I am a fan of the book [*Statistical Rethinking*](https://xcelab.net/rm/statistical-rethinking/), so I port the codes of [its second edition](https://github.com/rmcelreath/statrethinking_winter2019#draft-chapters) to [NumPyro](https://github.com/pyro-ppl/numpyro). I hope that the book and this translation will be helpful not only for NumPyro/Pyro users but also for ones who are willing to do Bayesian statistics in Python.

## Contents

{{% contents %}}

## Supplements

+ [data](data/)

+ [source](https://github.com/fehiepsi/rethinking-numpyro)

## Installation

The following tools are used for some analysis and visualizations: [arviz](https://arviz-devs.github.io/arviz/) for [posteriors](https://en.wikipedia.org/wiki/Posterior_probability), [causalgraphicalmodels](https://github.com/ijmbarr/causalgraphicalmodels) for [causal graphs](https://en.wikipedia.org/wiki/Causal_graph), [ete3](http://etetoolkit.org/) for [phylogenetic trees](https://en.wikipedia.org/wiki/Phylogenetic_tree).

```sh
pip install numpyro arviz causalgraphicalmodels ete3
```
