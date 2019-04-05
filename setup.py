#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import setuptools 

with open("README.rst", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="secretpy",
	version="0.6.1",
	author="Max Vetrov",
	author_email="maxvetrov555@yandex.ru",
	description="Classic ciphers package",
	long_description=long_description,
	long_description_content_type="text/x-rst",
	url="https://github.com/tigertv/secretpy",
	packages=setuptools.find_packages(exclude=['tests','tests.*']),
	test_suite='tests',
	project_urls={
		"Source code": "https://github.com/tigertv/secretpy",
		"Documentation": "https://secretpy.readthedocs.io",
		"Bug tracker": "https://github.com/tigertv/secretpy/issues",
	},
	classifiers=[
		'Development Status :: 3 - Alpha',
		'License :: OSI Approved :: MIT License',
		'Intended Audience :: Developers',
		'Intended Audience :: Education',
		'Intended Audience :: Science/Research',
		'Intended Audience :: End Users/Desktop',
		'Intended Audience :: Other Audience',
		'Topic :: Security :: Cryptography',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Education',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: Implementation :: CPython',
		'Programming Language :: Python :: Implementation :: PyPy',
	],
	keywords="classic ciphers cipher secret",
)
