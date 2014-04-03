#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import unittest

import shellstyle


class TestShellStyle(unittest.TestCase):

    def setUp(self):
        CURDIR = os.path.dirname(__file__)
        self.ifconfig_out_path = os.path.join(CURDIR, 'data/ifconfig.out')

    def tearDown(self):
        pass

    def test_single_run(self):
        re = shellstyle.run('echo hello shellstyle').stdout()
        self.assertEqual(re, 'hello shellstyle\n')

    def test_simple_pipe(self):
        re = shellstyle.run('echo yes no').p("awk '{print $1}'").stdout()
        self.assertEqual(re, 'yes\n')

    def test_inputstream(self):
        in_str = open(self.ifconfig_out_path).read()
        re = shellstyle.inputstream(in_str).p('grep eth0').stdout()
        self.assertEqual(re, 'eth0      Link encap:Ethernet  HWaddr 00:30:ac:c9:2e:f4\n')

    def test_chain_of_pipe(self):
        re = shellstyle.run('cat {0}'.format(self.ifconfig_out_path))\
                .p("grep -A 1 eth0")\
                .p("grep inet")\
                .p("awk '{print $2}'")\
                .p("cut -d: -f 2").stdout()
        self.assertEqual(re, '192.168.116.101\n')
        re = (shellstyle
                .run('cat {0}'.format(self.ifconfig_out_path))
                .p("grep -A 1 lo")
                .p("grep inet")
                .p("awk '{print $2}'")
                .p("cut -d: -f 2")
                .stdout())
        self.assertEqual(re, '127.0.0.1\n')

    def test_pipe_all(self):
        re = shellstyle.pipe_all([
                'cat {0}'.format(self.ifconfig_out_path),
                'grep -A 1 eth0',
                'grep inet',
                'awk \'{print $2}\'',
                'cut -d: -f 2']).stdout()
        self.assertEqual(re, '192.168.116.101\n')


if __name__ == "__main__":
    unittest.main()


