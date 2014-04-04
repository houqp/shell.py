# -*- coding:utf-8 -*-

import sys
from .run_cmd import RunCmd
from .input_stream import InputStream


def inputstream(s):
    return InputStream(s)


def cmd(cmd_str):
    return RunCmd(cmd_str)


def pipe_all(cmd_lst):
    #@TODO support first element as inputstream  03.04 2014 (houqp)
    ssr = RunCmd(cmd_lst.pop(0))
    for cmd in cmd_lst:
        ssr = ssr.p(cmd)
    return ssr


def p(arg):
    if type(arg) == str:
        return cmd(arg)
    elif type(arg) == list:
        return pipe_all(arg)


def ex(cmd_str):
    return RunCmd(cmd_str).run()
