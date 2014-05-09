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

Block until return:

.. code-block:: python

    >>> from shell import ex
    >>> ex('echo hello shell.py').stdout()
    'hello shell.py\n'

Asynchronous execution:

.. code-block:: python

    >>> from shell import ex
    >>> c = asex('echo hello shell.py')
    >>> # do something else
    ...
    >>> c.stdout() # wait until process exit and read stdout
    'hello shell.py\n'



Pipe commands
.............

.. code-block:: python

    from shell import ex
    re = (ex("ifconfig")
          | "grep -A 1 eth0"
          | "grep inet"
          | "awk '{print $2}'"
          | "cut -d: -f 2").stdout()

Or

.. code-block:: python

    from shell import pipe_all
    pipe_all(["ls -la ~",
              "awk '{print $9}'",
              "grep -E '^\.'",
              "wc -l"]).stdout()


Use string as stdin
...................

.. code-block:: python

    >>> from shell import instream
    >>> instream("1 2 3").p("awk '{print $1}'").stdout()
    '1\n'

This is equivalent to:

.. code-block:: python

    >>> from shell import ex
    >>> ex("echo 1 2 3").p("awk '{print $1}'").stdout()


IO redirect
............

Overwrite a file:

.. code-block:: python

    >>> from shell import ex
    >>> ex('echo yolo').wr('/tmp/out')
    >>> ex('echo yolo') > '/tmp/out'

Append to a file:

.. code-block:: python

    >>> from shell import ex
    >>> ex('echo yolo').ap('/tmp/out')
    >>> ex('echo yolo') >> '/tmp/out'


Run commands in parallel
........................

Block until all commands return:

.. code-block:: python

    >>> from shell import parallel as par
    >>> par.ex_all(['sleep 2', 'sleep 2']) # return in 2s

Asynchronous parallel execution:

.. code-block:: python

    >>> from shell import parallel as par
    >>> pe = par.asex_all(['sleep 2', 'sleep 2']) # return immediately
    >>> # do something else
    ...
    >>> pe.wait()


See test cases for more examples.


Tests
-----

Run tests with nosetests(at least v1.3.0):

.. code-block:: bash

    $ make test


