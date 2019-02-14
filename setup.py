#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import setuptools 

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
    name="secretpy",
    version="0.0.6",
    author="Max Vetrov",
    author_email="maxvetrov555@yandex.ru",
    description="Classic ciphers package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tigertv/secretpy",
    packages=setuptools.find_packages(exclude=['tests','tests.*']),
	test_suite='tests',
    classifiers=[
		'Development Status :: 3 - Alpha',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Intended Audience :: Developers',
		'Intended Audience :: Science/Research',
		'Intended Audience :: End Users/Desktop',
		'Intended Audience :: Other Audience',
		'Topic :: Security :: Cryptography',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
	],
)
