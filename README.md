# Anomaly free package

![Python package](https://github.com/anacmolina/anomaly_free/workflows/Python%20package/badge.svg)
![Upload Python Package](https://github.com/anacmolina/anomaly_free/workflows/Upload%20Python%20Package/badge.svg)

This package implements the general solution to the $U(1)$ anomaly equations the solution develop in [arXiv:1905.13729](https://arxiv.org/pdf/1905.13729.pdf) to find severals sets of $n$ integers that follows

$$ z_{1} + ... + z_{n} = 0 $$

$$ z_{1}^{3} + ... + z_{n}^{3} = 0 $$

where $|z_i|<|z_{max}|$.

## Prerequisites

Requirements 
- [Numpy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Dask](https://www.dask.org/)

## Install
```bash
$ pip install -i https://test.pypi.org/simple/ anomaly-free
```

## USAGE
```bash
anomaly_free --N=50000 --m=6 --zmax=30 --imax=0 --output_file=solution 5
```

To guess a $N$ values for you $n$ you can run:
```bash
anomaly_free --suggested_N 5
```

### Author
[anacmolina](https://github.com/anacmolina)


