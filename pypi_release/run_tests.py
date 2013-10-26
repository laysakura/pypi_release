# -*- coding: utf-8 -*-
"""run tests"""
import shlex
import subprocess
from pypi_release.errors import CmdError
from pypi_release.utils import setup_py_path


def run(test_cmd):
    cmd = "%s %s" % (setup_py_path(), test_cmd)
    retcode = subprocess.call(shlex.split(cmd))
    if retcode != 0:
        raise CmdError('`%s` failed...' % (test_cmd))
