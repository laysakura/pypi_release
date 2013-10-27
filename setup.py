#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name             = 'pypi_release',
    description      = '`setup.py release` command to support releasing your PyPI packages',
    long_description = open('README.rst').read(),
    url              = 'https://github.com/laysakura/pypi_release',
    license          = 'LICENSE.txt',
    version          = '0.1',
    author           = 'Sho Nakatani',
    author_email     = 'lay.sakura@gmail.com',
    test_suite       = 'nose.collector',
    install_requires = [
        'verlib',
        'nextversion',
    ],
    tests_require    = [
        'nose',
        'coverage',
    ],
    packages         = [
        'pypi_release',
        'pypi_release.test'
    ],
    classifiers      = '''
Programming Language :: Python
Development Status :: 5 - Production/Stable
Environment :: Plugins
Intended Audience :: Developers
Topic :: Software Development :: Libraries :: Python Modules
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.3
License :: OSI Approved :: Apache Software License
'''.strip().splitlines()
)
