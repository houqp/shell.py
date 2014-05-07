#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tempfile

from .compat import is_py2, is_py3


def str_to_pipe(s):
    input_pipe = tempfile.SpooledTemporaryFile()
    if (is_py2 and isinstance(s, unicode)) or (is_py3 and isinstance(s, str)):
        s = s.encode('utf-8')
    input_pipe.write(s)
    input_pipe.seek(0)
    return input_pipe


def check_attrs(obj, attr_lst):
    return all([hasattr(obj, attr) for attr in attr_lst])


if is_py3:
    def u(x):
        return x
else:
    import codecs

    def u(x):
        return codecs.unicode_escape_decode(x)[0]
