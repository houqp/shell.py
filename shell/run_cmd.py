#!/usr/bin/env python
# -*- coding:utf-8 -*-

import locale
import io
import os
import shlex
from subprocess import Popen
from subprocess import PIPE

from .compat import basestring
from .util import str_to_pipe, check_attrs


def is_seekable(target):
    # assume if it doesn't have seekable() method, .e.g a file object, then its
    # seekable
    return ((not hasattr(target, 'seekable') and hasattr(target, 'seek')) or
            (hasattr(target, 'seekable') and target.seekable()))


def parse_shell_token(t):
    if t[0] == "'" and t[-1] == "'":
        return t[1:-1]
    elif t[0] == '"' and t[-1] == '"':
        t = t[1:-1]
    # handle '~'
    t = os.path.expanduser(t)
    # handle env var
    t = os.path.expandvars(t)
    return t


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
        return [parse_shell_token(t)
                for t in shlex.split(self.cmd_str, posix=False)]

    def init_popen(self):
        if self.cmd_p is None:
            self.cmd_p = Popen(
                self.get_cmd_lst(),
                stdin=self.input_pipe, stdout=PIPE, stderr=PIPE)
        return self

    def get_popen(self):
        return self.init_popen().cmd_p

    def p(self, cmd):
        # @TODO check cmd
        in_pipe = None
        cmd_p = self.get_popen()
        if cmd_p.stdout.closed:
            # command has already been executed, get output as string
            in_pipe = str_to_pipe(self.std['out'])
        else:
            in_pipe = cmd_p.stdout
        # cmd_p.stdout.close() # allow cmd_p to receive SIGPIPE?
        return RunCmd(cmd, input_pipe=in_pipe)

    def wait(self):
        cmd_p = self.get_popen()
        if cmd_p.returncode is None:
            self.std['out'], self.std['err'] = cmd_p.communicate()
        return self

    def poll(self):
        """
        return None if not terminated, otherwise return return code
        """
        cmd_p = self.get_popen()
        return cmd_p.poll()

    def stdout(self):
        if self.std['out'] is None:
            self.wait()
        return self.std['out']

    def stderr(self):
        if self.std['err'] is None:
            self.wait()
        return self.std['err']

    def re(self):
        self.wait()
        return self.cmd_p.returncode

    def __or__(self, other):
        if isinstance(other, basestring):
            return self.p(other)
        elif isinstance(other, RunCmd):
            return self.p(other.cmd_str)
        raise ValueError('argument must be a string or an instance of RunCmd')

    def wr(self, target, source='stdout'):
        if source != 'stdout' and source != 'stderr':
            raise ValueError('unsupported source: {0}'.format(source))

        out = getattr(self, source)()

        if isinstance(target, basestring):
            fd = open(target, 'wb')
            fd.write(out)
            fd.close()
        elif isinstance(target, io.TextIOBase):
            target.truncate(0)
            encoding = target.encoding if target.encoding is not None \
                else locale.getpreferredencoding(False)
            target.write(out.decode(encoding))
        elif check_attrs(target, ['write', 'truncate', 'seek']):
            target.truncate(0)
            if is_seekable(target):  # work around bug in pypy<2.3.0-alpha0
                target.seek(0, os.SEEK_SET)
            target.write(out)
        else:
            raise ValueError('first argument must be a string '
                             'or has (write, truncate) methods')

    def __gt__(self, target):
        self.wr(target)

    def ap(self, target, source='stdout'):
        if source != 'stdout' and source != 'stderr':
            raise ValueError('unsupported source: {0}'.format(source))

        out = getattr(self, source)()

        if isinstance(target, basestring):
            fd = open(target, 'ab')
            fd.write(out)
            fd.close()
        elif isinstance(target, io.TextIOBase):
            encoding = target.encoding if target.encoding is not None \
                else locale.getpreferredencoding(False)
            target.write(out.decode(encoding))
        elif check_attrs(target, ['write', 'seek']):
            if is_seekable(target):  # work around bug in pypy<2.3.0-alpha0
                target.seek(0, os.SEEK_END)
            target.write(out)
        else:
            raise ValueError('first argument must be a string '
                             'or has (write, seek) methods')

    def __rshift__(self, target):
        self.ap(target)
