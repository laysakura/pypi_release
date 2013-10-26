# -*- coding: utf-8 -*-
"""exception classes"""


class BaseError(Exception):
    """Base class for exceptions in this module."""
    pass


class CmdError(BaseError):
    """An exception raised when subprocess failed."""
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
