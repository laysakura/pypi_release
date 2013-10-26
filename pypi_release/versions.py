# -*- coding: utf-8 -*-
"""fetching/updating version strings"""


import commands
from pypi_release.errors import CmdError
from pypi_release.utils import setup_py_path


def get_current_version():
    """Get current version of package in cwd"""
    cmd = "%s --version" % (setup_py_path())
    return commands.getoutput(cmd)
