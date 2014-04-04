#!/usr/bin/env python

import os
import sys

import shell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'shell',
]

requires = []

setup(
    name='shell',
    version=shell.__version__,
    description='Shell power for Python.',
    #long_description=readme + '\n\n' + history,
    author='Qingping Hou',
    author_email='dave2008713@gmail.com',
    #url='http://fooo.org',
    packages=packages,
    #package_data={'': ['LICENSE', 'NOTICE'], 'requests': ['*.pem']},
    package_dir={'shell': 'shell'},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
