# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup, find_packages


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name="csvputty",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        csvputty=csvputty.__main__:cli
    ''',
    version='0.1.0',
    description="CSV CLI utility functions and packages in Python.",
    long_description=long_descr,
    author="Anthony Manning-Franklin",
    author_email="anthony.manning.franklin@gmail.com",
    url="",
)
