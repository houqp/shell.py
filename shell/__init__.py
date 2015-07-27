#!/usr/bin/env python
# -*- coding:utf-8 -*-

__title__ = 'shell'
__version__ = '0.5.3'
__author__ = 'Qingping Hou'
__license__ = 'MIT'

from .run_cmd import RunCmd  # noqa
from .input_stream import InputStream  # noqa
from .api import env, instream, ex, ex_all, asex, pipe_all, p, cwd  # noqa
from . import parallel_api as parallel  # noqa
