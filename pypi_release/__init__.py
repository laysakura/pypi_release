# -*- coding: utf-8 -*-
"""
    pypi_release
    ~~~~~~~~~~~~

    `setup.py release` command to support releasing your PyPI packages
"""


from distutils.cmd import Command
import os
import sys
import shlex
import subprocess


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

    _SETUP_PY   = 'setup.py'
    _MSG_PROMPT = '[release] '

    def initialize_options(self):
        self.changes_file = None
        self.version      = None
        self.test_cmd     = None

        self.no_test = False

    def finalize_options(self):
        # changelogのフルパスセット
        # next version を何とか探してきてセット
        self.version = '10.0.0'

        if not self.test_cmd:
            self.test_cmd = 'test'

    def run(self):
        print("Hello from release.py")

        # run test
        Release._msg('Running tests with `%s` command...\n' % (self.test_cmd))
        if not self.no_test:
            Release._run_test(self.test_cmd)

        # check next version
        Release._msg('Enter next version string [%s]: ' % self.version)
        v = raw_input().strip()
        if v != '':
            self.version = v

        

    # Helper functions
    @staticmethod
    def _run_test(test_cmd):
        cmd = "%s %s" % (Release._setup_py_path(), test_cmd)
        retcode = subprocess.call(shlex.split(cmd))
        if retcode != 0:
            raise Exception('`%s` failed...' % (test_cmd))

    @staticmethod
    def _msg(msg):
        sys.stderr.write(Release._MSG_PROMPT + msg)
