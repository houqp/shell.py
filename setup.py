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

with open('README.rst') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()

setup(
    name='shell.py',
    version=shell.__version__,
    description='Shell power for Python.',
    # long_description=readme + '\n\n' + history,
    long_description=readme,
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
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ),
)
