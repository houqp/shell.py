#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tempfile


def str_to_pipe(s):
    input_pipe = tempfile.SpooledTemporaryFile()
    if isinstance(s, str):
        s = s.encode('utf-8')
    input_pipe.write(s)
    input_pipe.seek(0)
    return input_pipe
