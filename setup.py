#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="gpio4",
    version="0.0.1",
    author="AlexProgrammerDE",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/hankso/gpio4",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "License :: Apache License 2.0",
        "Programming Language :: Python",
        "Topic :: System :: Hardware :: Hardware Drivers :: Bluetooth"
    ]
)
