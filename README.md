[![Test Status](https://github.com/fehiepsi/rethinking-numpyro/workflows/CI/badge.svg)](https://github.com/fehiepsi/rethinking-numpyro/actions)
# Statistical Rethinking (2nd ed.) with NumPyro

I am a fan of the book [*Statistical Rethinking*](https://xcelab.net/rm/statistical-rethinking/), so I port the codes of [its second edition](https://github.com/rmcelreath/rethinking) to [NumPyro](https://github.com/pyro-ppl/numpyro). I hope that the book and this translation will be helpful not only for NumPyro/Pyro users but also for ones who are willing to do Bayesian statistics in Python. 

## How to read the notebooks

+ Read on the site: https://fehiepsi.github.io/rethinking-numpyro/

+ Use GitHub's renderer: https://github.com/fehiepsi/rethinking-numpyro/tree/master/notebooks/

+ Use Jupyter's nbviewer: https://nbviewer.jupyter.org/github/fehiepsi/rethinking-numpyro/tree/master/notebooks/

## Installation

The following tools are used for some analysis and visualizations: [arviz](https://arviz-devs.github.io/arviz/) for [posteriors](https://en.wikipedia.org/wiki/Posterior_probability), [networkx](https://networkx.org/) and [daft](https://docs.daft-pgm.org/en/latest/) for [causal graphs](https://en.wikipedia.org/wiki/Causal_graph), and (optional) [ete3](http://etetoolkit.org/) for [phylogenetic trees](https://en.wikipedia.org/wiki/Phylogenetic_tree).

```sh
pip install numpyro arviz daft networkx
```

## Excercises

If you need help solving the exercises with numpyro, there are resolutions from chapter 2 and 3 [here](https://github.com/felipeffm/statistical-rethinking-resolutions).

## Acknowledgements

[Kapil Sachdeva](https://github.com/ksachdeva) and [Manuel A. Vázquez](https://github.com/manuvazquez) has helped fix many code and plot mismatches since the release. Many thanks!
