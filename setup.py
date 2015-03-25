#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()

setup(
    name='pytest-stepwise',
    version='0.3',
    author='Niclas Olofsson',
    author_email='n@niclasolofsson.se',
    maintainer='Niclas Olofsson',
    maintainer_email='n@niclasolofsson.se',
    license='MIT',
    url='https://github.com/nip3o/pytest-stepwise',
    description='Run a test suite one failing test at a time.',
    long_description=read('README.rst'),
    py_modules=['pytest_stepwise'],
    install_requires=['pytest-cache >= 1.0'],
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'Topic :: Software Development :: Testing',
                 'Programming Language :: Python',
                 'Operating System :: OS Independent',
                 'License :: OSI Approved :: MIT License'],
    entry_points={'pytest11': ['stepwise = pytest_stepwise']},
)
