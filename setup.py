#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import setuptools 

setuptools.setup(
    name="secretpy",
    version="0.0.1",
    author="Max Vetrov",
    author_email="maxvetrov555@yandex.ru",
    description="Classic ciphers package",
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tigertv/secretpy",
    packages=setuptools.find_packages(exclude=['tests','tests.*']),
	test_suite='tests',
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
