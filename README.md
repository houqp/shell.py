
shell.py
========

Bring the good part of Shell scripting to Python.


Install
-------
```
pip install shell.py
```

Usage
-----

#### Execute a shell command

```python
>>> from shell import ex
>>> ex('echo hello shell.py').stdout()
'hello shell.py\n'
```

#### Pipe commands

```python
from shell import p
pipeline = (p('ifconfig')
			.p('grep -A 1 eth0')
			.p('grep inet')
			.p('awk "{print $2}"')
			.p('cut -d: -f 2'))
print pipeline.stdout()
```

Or

```python
from shell import pipe_all
pipeline = shell.pipe_all(['ifconfig',
                           'grep -A 1 eth0',
                           'grep inet',
                           'awk "{print $2}"',
                           'cut -d: -f 2'])
print pipeline.stdout()
```

#### Use string as command input

```python
>>> from shell import input_stream
>>> input_stream('1 2 3').p('awk "{print $1}"').stdout()
'1\n'
```
This is equivalent to `ex('echo 1 2 3').p('awk "{print $1}"').stdout()`.

See test cases for more examples.


Tests
-----

Run tests with nosetests(at least v1.3.0):

```
make test
```


