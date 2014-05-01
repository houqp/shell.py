#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import shlex
from subprocess import Popen
from subprocess import PIPE

from .util import str_to_pipe

class RunCmd():
    def __init__(self, cmd_str, input_pipe=None):
        self.cmd_str = cmd_str
        self.cmd_p = None
        if input_pipe:
            self.input_pipe = input_pipe
        else:
            self.input_pipe = None
        self.std = {'out': None, 'err': None}

    def get_cmd_lst(self):
        # handle '~'
        lst = [os.path.expanduser(c) for c in shlex.split(self.cmd_str)]
        #@TODO handl env var  03.04 2014 (houqp)
        return lst

    def get_popen(self):
        if self.cmd_p is None:
            self.cmd_p = Popen(
                    self.get_cmd_lst(),
                    stdin=self.input_pipe, stdout=PIPE, stderr=PIPE)
        return self.cmd_p

    def p(self, cmd):
        in_pipe = None
        if self.std['out']:
            # command has already been executed, get output as string
            in_pipe = str_to_pipe(self.std['out'])
        else:
            cmd_p = self.get_popen()
            in_pipe = cmd_p.stdout
        #cmd_p.stdout.close() # allow cmd_p to receive SIGPIPE?
        return RunCmd(cmd, input_pipe=in_pipe)

    def run(self):
        cmd_p = self.get_popen()
        if cmd_p.returncode is None:
            self.std['out'], self.std['err'] = cmd_p.communicate()
        return self

    def stdout(self):
        if self.std['out'] is None:
            self.run()
        return self.std['out']

    def stderr(self):
        if self.std['err'] is None:
            self.run()
        return self.std['err']

    def re(self):
        self.run()
        return self.cmd_p.returncode


