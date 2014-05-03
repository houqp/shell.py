#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import unittest
import subprocess
import shell


class TestShellStyle(unittest.TestCase):

    def setUp(self):
        CURDIR = os.path.dirname(__file__)
        self.data_dir_path = os.path.join(CURDIR, 'data')
        self.ifconfig_out_path = os.path.join(self.data_dir_path,
                                              'ifconfig.out')
        self.test_out_file = os.path.join(self.data_dir_path, 'test_out')

    def tearDown(self):
        pass

    def test_single_run_retcode(self):
        self.assertEqual(shell.p('echo hello shell.py').re(), 0)
        self.assertNotEqual(shell.p('ls wtf#noneexist#dir#yay').re(), 0)

    def test_single_run_stdout(self):
        re = shell.p('echo hello shell.py').stdout()
        self.assertEqual(re, b'hello shell.py\n')

    def test_multiple_ex(self):
        re = shell.ex_all([
            'echo hello',
            'echo world'])
        self.assertEqual(re[0].stdout(), b'hello\n')
        self.assertEqual(re[1].stdout(), b'world\n')

    def test_single_run_stderr(self):
        bad_path = 'wtf#noneexist#dir#yay'
        expected_stderr = subprocess.Popen(
            ['ls', bad_path], stderr=subprocess.PIPE).communicate()[1]
        task = shell.ex('ls {0}'.format(bad_path))
        self.assertNotEqual(task.re(), 0)
        self.assertEqual(task.stderr(), expected_stderr)

    def test_simple_pipe(self):
        pipeline = shell.p('echo yes no').p("awk '{print $1}'")
        self.assertEqual(pipeline.stdout(), b'yes\n')
        self.assertEqual(pipeline.re(), 0)

    def test_simple_pipe_run(self):
        pipeline = shell.p('echo yes no').p("awk '{print $1}'")
        pipeline.run()
        self.assertEqual(pipeline.stdout(), b'yes\n')
        self.assertEqual(pipeline.re(), 0)

    def test_instream(self):
        in_str = open(self.ifconfig_out_path).read()
        self.assertEqual(
            shell.instream(in_str).p('grep eth0').stdout(),
            b'eth0      Link encap:Ethernet  HWaddr 00:30:ac:c9:2e:f4\n')

    def test_chain_of_pipe(self):
        pipeline = shell.p('cat {0}'.format(self.ifconfig_out_path))\
                        .p("grep -A 1 eth0")\
                        .p("grep inet")\
                        .p("awk '{print $2}'")\
                        .p("cut -d: -f 2")
        self.assertEqual(pipeline.stdout(), b'192.168.116.101\n')
        self.assertEqual(pipeline.re(), 0)
        pipeline = (shell
                    .p('cat {0}'.format(self.ifconfig_out_path))
                    .p("grep -A 1 lo")
                    .p("grep inet")
                    .p("awk '{print $2}'")
                    .p("cut -d: -f 2"))
        self.assertEqual(pipeline.stdout(), b'127.0.0.1\n')
        self.assertEqual(pipeline.re(), 0)

    def test_chain_of_pipe_using_operator_overloading(self):
        pipeline = (shell.RunCmd('cat {0}'.format(self.ifconfig_out_path))
                    | shell.RunCmd("grep -A 1 eth0")
                    | shell.RunCmd("grep inet")
                    | shell.RunCmd("awk '{print $2}'")
                    | shell.RunCmd("cut -d: -f 2"))
        self.assertEqual(pipeline.stdout(), b'192.168.116.101\n')
        self.assertEqual(pipeline.re(), 0)

        pipeline = (shell.RunCmd('cat {0}'.format(self.ifconfig_out_path))
                    | "grep -A 1 lo"
                    | "grep inet"
                    | "awk '{print $2}'"
                    | "cut -d: -f 2")
        self.assertEqual(pipeline.stdout(), b'127.0.0.1\n')
        self.assertEqual(pipeline.re(), 0)

    def test_pipe_with_cmd_list(self):
        pipeline = shell.pipe_all(['cat {0}'.format(self.ifconfig_out_path),
                                   'grep -A 1 eth0',
                                   'grep inet',
                                   'awk "{print $2}"',
                                   'cut -d: -f 2'])
        self.assertEqual(pipeline.stdout(), b'192.168.116.101\n')
        self.assertEqual(pipeline.re(), 0)
        pipeline = shell.p(['cat {0}'.format(self.ifconfig_out_path),
                            'grep -A 1 eth0',
                            'grep inet',
                            'awk "{print $2}"',
                            'cut -d: -f 2'])
        self.assertEqual(pipeline.stdout(), b'192.168.116.101\n')
        self.assertEqual(pipeline.re(), 0)

    def test_ex_pipe(self):
        out = shell.ex('echo -e "123\n456\n789"').p('grep 4').stdout()
        self.assertEqual(out, b'456\n')

    def test_expand_tilde(self):
        task = shell.ex('echo ~')
        self.assertEqual(task.re(), 0)
        self.assertEqual(task.stdout(),
                         (os.path.expanduser('~')+'\n').encode('utf-8'))

    def test_io_redirect_wr_string_arg(self):
        shell.ex('rm -rf {0}'.format(self.test_out_file))
        shell.ex('echo 123').wr(self.test_out_file)
        out_content = shell.ex('cat {0}'.format(self.test_out_file)).stdout()
        self.assertEqual(b'123\n', out_content)
        os.remove(self.test_out_file)

    def test_io_redirect_wr_file_arg(self):
        shell.ex('rm -rf {0}'.format(self.test_out_file))
        fd = open(self.test_out_file, 'wb')
        shell.ex('echo 123').wr(fd)
        fd.close()
        out_content = shell.ex('cat {0}'.format(self.test_out_file)).stdout()
        self.assertEqual(b'123\n', out_content)
        os.remove(self.test_out_file)


if __name__ == "__main__":
    unittest.main()
