#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tempfile
from .run_cmd import RunCmd

class InputStream():
    def __init__(self, input_str):
        self.input_pipe = tempfile.SpooledTemporaryFile()
        self.input_pipe.write(input_str)
        self.input_pipe.seek(0)

    def p(self, cmd):
        return RunCmd(cmd, input_pipe=self.input_pipe)


