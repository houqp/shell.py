#!/usr/bin/env python
# -*- coding:utf-8 -*-

__title__ = 'shell'
__version__ = '0.0.1'
__author__ = 'Qingping Hou'
__license__ = 'MIT'

from .run_cmd import RunCmd
from .input_stream import InputStream
from .api import inputstream, cmd, pipe_all, ex, p