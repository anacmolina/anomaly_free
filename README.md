# Anomaly free

![Python package](https://github.com/anacmolina/anomaly_free/workflows/Python%20package/badge.svg)
![Upload Python Package](https://github.com/anacmolina/anomaly_free/workflows/Upload%20Python%20Package/badge.svg)

This package implements the general solution to the $U(1)$ anomaly equations the solution develop in [arXiv:1905.13729](https://arxiv.org/pdf/1905.13729.pdf) to find 

$$ z_1**3 + ... + z_n**3 = 0 $$

severals sets of $n$ integers, where $|z_i|<|zmax|$.

### Prerequisites

Requirements 
- [Numpy](https://www.example.com)
- [Pandas](https://www.example.com)
- [Multiprocessing](https://www.example.com)
- [Dask](https://www.example.com)

### Installing

pip install 

### Running 

Default values:

anomaly_free --N=50000 --m=6 --zmax=30 --imax=0 --output_file=solution 5

To guess a $N$ values for you $n$ you can run:

anomaly_free --suggested_N 5

### Sample Tests

anomaly_free 5
anomaly_free 6

## Authors

  - **Ana Cristina Molina** - *Provided README Template* -
    [anacmolina](https://github.com/anacmolina)


## License

This project is licensed under the [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details

