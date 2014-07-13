#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='pytest-stepwise',
    version='0.1',
    author='Niclas Olofsson',
    author_email='n@niclasolofsson.se',
    maintainer='Niclas Olofsson',
    maintainer_email='n@niclasolofsson.se',
    description='Run a test suite one failing test at a time.',
    py_modules=['pytest_stepwise'],
    install_requires=['pytest-cache >= 1.0'],
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'Topic :: Software Development :: Testing',
                 'Programming Language :: Python'],
    entry_points={'pytest11': ['stepwise = pytest_stepwise']},
)
