#!/usr/bin/env python3
# coding: utf-8

# Copyright (c) Colav.
# Distributed under the terms of the Modified BSD License.

# -----------------------------------------------------------------------------
# Minimal Python version sanity check (from IPython)
# -----------------------------------------------------------------------------

# See https://stackoverflow.com/a/26737258/2268280
# sudo pip3 install twine
# python3 setup.py sdist bdist_wheel
# twine upload dist/*
# For test purposes
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

from __future__ import print_function
from setuptools import setup, find_packages

import os
import sys


v = sys.version_info

shell = False
if os.name in ('nt', 'dos'):
    shell = True
    warning = "WARNING: Windows is not officially supported"
    print(warning, file=sys.stderr)


def main():
    setup(
        # Application name:
        name="anomaly_free",

        # Version number (initial):
        version="0.0.1",

        # Application author details:
        author="anacmolina",
        author_email="anac.molina@udea.edu.co",

        # Packages
        packages=find_packages(exclude=['tests']),

        # Include additional files into the package
        include_package_data=True,

        # Details
        url="https://github.com/anacmolina/anomaly_free",
        scripts=['bin/anomaly_free'],

        license="BSD",

        description="Anomalies U(1)",

        long_description=open("README.md").read(),

        long_description_content_type="text/markdown",

        # Dependent packages (distributions)
        # See: https://github.com/pypa/pipenv/issues/2171
        install_requires=['numpy==1.16.5; python_version=="3.7"',
            'numpy>=1.16.5; python_version=="3.8"',
            'numpy>=1.16.5; python_version=="3.9"'],
        install_requires=['pandas'],
        requires=['pandas'],
    )


if __name__ == "__main__":
    main()