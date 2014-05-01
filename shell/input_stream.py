#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .run_cmd import RunCmd
from .util import str_to_pipe

class InputStream():
    def __init__(self, input_str):
        self.input_pipe = str_to_pipe(input_str)

    def p(self, cmd):
        return RunCmd(cmd, input_pipe=self.input_pipe)


