# -*- coding:utf-8 -*-

import os
from contextlib import contextmanager
from .compat import basestring
from .run_cmd import RunCmd
from .input_stream import InputStream


def env(key):
    return os.environ.get(key)


def instream(s):
    return InputStream(s)


def ex(cmd_str):
    """Execute a shell command.

    Args:
        cmd_str: shell command as string.

    Returns:
        A RunCmd instance.
    """
    return RunCmd(cmd_str).wait()


def ex_all(cmd_lst):
    return [ex(c) for c in cmd_lst]


def asex(cmd_str):
    return RunCmd(cmd_str).init_popen()


def pipe_all(cmd_lst):
    # @TODO support first element as inputstream  03.04 2014 (houqp)
    ssr = RunCmd(cmd_lst.pop(0))
    for cmd in cmd_lst:
        ssr = ssr.p(cmd)
    return ssr


def p(arg):
    if isinstance(arg, basestring):
        return RunCmd(arg)
    elif isinstance(arg, list):
        return pipe_all(arg)
    else:
        raise ValueError('argument must be a string or list')

#could use ContextDecorator (built in python 3.2, pypi for python 2)
#to allow this context manager to work as a decorator as well
@contextmanager
def cwd(new_dir):
    """Used with with, temporarily change the current working directory
    Raises:
        OSError: error changing directory
    """
    saved_cwd = os.getcwd()
    #handle path beginning with ~
    os.chdir(os.path.expanduser(new_dir))
    try:
        yield saved_cwd
    finally:
        os.chdir(saved_cwd)
