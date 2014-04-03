# -*- coding:utf-8 -*-

import sys
from .run_cmd import RunCmd
from .input_stream import InputStream


def inputstream(s):
    return InputStream(s)


def run(cmd_str):
    return RunCmd(cmd_str)


def pipe_all(cmd_lst):
    #@TODO support first element as inputstream  03.04 2014 (houqp)
    ssr = RunCmd(cmd_lst.pop(0))
    for cmd in cmd_lst:
        ssr = ssr.p(cmd)
    return ssr


