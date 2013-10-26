# -*- coding: utf-8 -*-
"""utility functions"""


import os


def setup_py_path():
    """Get absolute path of executable `setup.py` from cwd with check

    :returns: absolute path of `setup.py`
    :raises:  IOError, OSError
    """
    SETUP_PY = 'setup.py'
    if not os.path.exists(SETUP_PY):
        raise IOError('Cannot find `%s` from current directory' % (SETUP_PY))
    p = os.path.abspath(SETUP_PY)

    if not os.access(p, os.X_OK):
        raise OSError('`%s` is not executable' % (SETUP_PY))

    return p
