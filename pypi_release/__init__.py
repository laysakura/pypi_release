# -*- coding: utf-8 -*-
"""
    pypi_release
    ~~~~~~~~~~~~

    `setup.py release` command to support releasing your PyPI packages
"""


from distutils.cmd import Command
import os
import sys
import pypi_release.run_tests
from pypi_release.versions import get_current_version


class Release(Command):
    """Distutils command to support release procedure to PyPI.
    """

    description = 'Release PyPI package forcing version and CHANGES updates'
    user_options = [
        ('changes-file=', None, 'Location of the ChangeLog file'),
        ('version=',      None, 'Next version number'),
        ('test-cmd=',     None, 'Subcommand of `setup.py` to run tests. (python setup.py XXXX)'),
        ('no-test',       None, 'release without running test beforehand'),
    ]
    boolean_options = ['no-test']

    _MSG_PROMPT = '[release] '

    def initialize_options(self):
        self.changes_file = None
        self.version      = None
        self.test_cmd     = None

        self.no_test = False

    def finalize_options(self):
        # changelogのフルパスセット

        self.version = get_current_version()

        if not self.test_cmd:
            self.test_cmd = 'test'

    def run(self):
        print("Hello from release.py")

        # run test
        Release._msg('Running tests with `%s` command...\n' % (self.test_cmd))
        if not self.no_test:
            pypi_release.run_tests.run(self.test_cmd)

        # check next version
        Release._msg('Enter next version string [%s]: ' % self.version)
        v = raw_input().strip()
        if v != '':
            self.version = v

        

    @staticmethod
    def _msg(msg):
        sys.stderr.write(Release._MSG_PROMPT + msg)
