#!/usr/bin/env python

from setuptools import setup

setup(
    name="chranalyzer",
    version="0.0.1",
    packages=[],
    entry_points={
        'console_scripts': ['chranalyzer = chranalyze.__main__:main']
    }
)