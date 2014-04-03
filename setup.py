#!/usr/bin/env python

import os
import sys

import shellstyle

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'shellstyle',
]

requires = []

setup(
    name='shellstyle',
    version=shellstyle.__version__,
    description='Shell the good part for Python.',
    #long_description=readme + '\n\n' + history,
    author='Qingping Hou',
    author_email='dave2008713@gmail.com',
    #url='http://fooo.org',
    packages=packages,
    #package_data={'': ['LICENSE', 'NOTICE'], 'requests': ['*.pem']},
    package_dir={'shellstyle': 'shellstyle'},
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
