# Anomaly free

This package implements the general solution to the U(1) anomaly equations the solution develop in [arXiv:1905.13729](https://arxiv.org/pdf/1905.13729.pdf) to find 

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

To calculate a guess N you can run:

anomaly_free --suggested_N 5

### Sample Tests

anomaly_free 5
anomaly_free 6

## Built With

  - [Contributor Covenant](https://www.contributor-covenant.org/) - Used
    for the Code of Conduct
  - [Creative Commons](https://creativecommons.org/) - Used to choose
    the license

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## Versioning

We use [Semantic Versioning](http://semver.org/) for versioning. For the versions
available, see the [tags on this
repository](https://github.com/PurpleBooth/a-good-readme-template/tags).

## Authors

  - **Billie Thompson** - *Provided README Template* -
    [PurpleBooth](https://github.com/PurpleBooth)

See also the list of
[contributors](https://github.com/PurpleBooth/a-good-readme-template/contributors)
who participated in this project.

## License

This project is licensed under the [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details

## Acknowledgments

  - Hat tip to anyone whose code is used
  - Inspiration
  - etc
