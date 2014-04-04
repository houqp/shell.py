#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import shlex
from subprocess import Popen
from subprocess import PIPE


class RunCmd():
    def __init__(self, cmd_str, input_pipe=None):
        self.cmd_str = cmd_str
        if input_pipe:
            self.input_pipe = input_pipe
        else:
            self.input_pipe = None

    def get_cmd_lst(self):
        # handle '~'
        lst = [os.path.expanduser(c) for c in shlex.split(self.cmd_str)]
        #@TODO handl env var  03.04 2014 (houqp)
        return lst

    def get_popen(self):
        return Popen(self.get_cmd_lst(), stdin=self.input_pipe, stdout=PIPE)

    def p(self, cmd):
        cmd_p = self.get_popen()
        #cmd_p.stdout.close() # allow cmd_p to receive SIGPIPE?
        return RunCmd(cmd, input_pipe=cmd_p.stdout)

    def stdout(self):
        cmd_p = self.get_popen()
        return cmd_p.communicate()[0]



