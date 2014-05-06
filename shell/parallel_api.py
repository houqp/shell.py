#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .parallel_exec import ParallelExec


def ex_all(cmd_str_lst):
    return ParallelExec(cmd_str_lst).wait()


def asex_all(cmd_str_lst):
    return ParallelExec(cmd_str_lst)
