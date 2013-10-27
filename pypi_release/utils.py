# -*- coding: utf-8 -*-
"""utility functions"""
import os
import sys
import verlib


def msg(message):
    """Output message to stderr with pypi_release prompt."""
    MSG_PROMPT = '[release] '
    sys.stderr.write(MSG_PROMPT + message)


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


def ask_yes_no(default):
    """Ask user yes or no.

    :param default: 'yes' or 'no'
    :returns:       'yes' or 'no'
    """
    assert(default in ('yes', 'no'))
    yn = raw_input().strip().lower()
    if yn in ('y', 'yes', 'yeah', 'yep', 'ya'):
        return 'yes'
    elif yn in ('n', 'no', 'non', 'never', 'neah'):
        return 'no'
    else:
        return 'default'


def ask_next_version(candidate_version):
    """Ask user next version string.

    :param candidate_version: candidate of next version string
    :returns:                 next version string
    """
    cand_ver = candidate_version
    while True:
        # ask user's input
        message = 'Enter next version string'
        if cand_ver is not None:
            message += ' [%s]' % (cand_ver)
        msg(message + ': ')
        v = raw_input().strip()

        # check if default version is used
        if v == '' and cand_ver is not None:
            v = cand_ver

        # check input version
        norm_ver = verlib.suggest_normalized_version(v)
        if norm_ver is None:
            msg('`%s` is not match with PEP 386. Really OK? [y/N]: ' % (v))
            yn = ask_yes_no(default='no')
            if yn == 'yes':
                return v
        elif norm_ver != v:
            msg('`%s` is not match with PEP 386. Use recommended `%s`? [Y/n]: ' % (v, norm_ver))
            yn = ask_yes_no(default='yes')
            if yn == 'yes':
                return norm_ver
        else:
            assert(norm_ver == v)
            return v
