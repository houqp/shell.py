#!/usr/bin/env python


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
    name='shell.py',
    version=shell.__version__,
    description='Shell power for Python.',
    long_description=open('README.md', 'r').read(),
    author='Qingping Hou',
    author_email='dave2008713@gmail.com',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'shell': 'shell'},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    url='https://github.com/houqp/shell.py',
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
