#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .api import asex


class ParallelExec:
    def __init__(self, cmd_str_lst):
        self.cmd_str_lst = cmd_str_lst
        self.runcmd_lst = [asex(cmd) for cmd in cmd_str_lst]

    def wait(self):
        for p in self.runcmd_lst:
            p.wait()
        return self

    def poll(self):
        all_done = True
        for p in self.runcmd_lst:
            if p.poll() is None:
                all_done = False
                break
        if all_done:
            return self.runcmd_lst
        else:
            return None

    def cmds(self):
        return self.runcmd_lst
