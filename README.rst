shell.py
========

.. image:: https://badge.fury.io/py/shell.py.png
    :target: http://badge.fury.io/py/shell.py

.. image:: https://travis-ci.org/houqp/shell.py.svg?branch=master
    :target: https://travis-ci.org/houqp/shell.py

Bring the good part of Shell scripting to Python.


Install
-------

.. code-block:: bash

    $ pip install shell.py


Usage
-----

Execute a shell command
.......................

.. code-block:: python

    >>> from shell import ex
    >>> ex('echo hello shell.py').stdout()
    'hello shell.py\n'


Pipe commands
.............

.. code-block:: python

    from shell import ex
    pipeline = (ex('ifconfig')
                | 'grep -A 1 eth0'
                | 'grep inet'
                | 'awk "{print $2}"'
                | 'cut -d: -f 2')
    print pipeline.stdout()

Or

.. code-block:: python

    from shell import pipe_all
    pipeline = pipe_all(['ifconfig',
                         'grep -A 1 eth0',
                         'grep inet',
                         'awk "{print $2}"',
                         'cut -d: -f 2'])
    print pipeline.stdout()


Use string as command input
...........................

.. code-block:: python

    >>> from shell import instream
    >>> instream('1 2 3').p('awk "{print $1}"').stdout()
    '1\n'

This is equivalent to:

.. code-block:: python

    >>> from shell import ex
    >>> ex('echo 1 2 3').p('awk "{print $1}"').stdout()


See test cases for more examples.


Tests
-----

Run tests with nosetests(at least v1.3.0):

.. code-block:: bash

    $ make test


