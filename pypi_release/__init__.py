# -*- coding: utf-8 -*-
"""
    pypi_release
    ~~~~~~~~~~~~

    `setup.py release` command to support releasing your PyPI packages
"""


from distutils.cmd import Command
import os
import sys
from nextversion import nextversion
import pypi_release.run_tests
from pypi_release.versions import get_current_version
from pypi_release.utils import setup_py_path


class Release(Command):
    """Distutils command to support release procedure to PyPI.
    """

    description = 'Release PyPI package forcing version and CHANGES updates'
    user_options = [
        ('version-files=', None, 'Files to replace old version strings. `setup.py` is included by default. (README.rst,your_pkg/__init__.py)'),
        ('changes-file=',  None, 'Location of the ChangeLog file'),
        ('version=',       None, 'Next version number'),
        ('test-cmd=',      None, 'Subcommand of `setup.py` to run tests. (./setup.py XXXX)'),
        ('no-test',        None, 'release without running test beforehand'),
    ]
    boolean_options = ['no-test']

    def initialize_options(self):
        self.version_files = None
        self.changes_file  = None
        self.version       = None
        self.test_cmd      = None

        self.no_test = False

    def finalize_options(self):
        # changelogのフルパスセット

        self.version_files = [setup_py_path()] + map(os.path.abspath, self.version_files.split(','))
        self.version       = nextversion(get_current_version())

        if not self.test_cmd:
            self.test_cmd = 'test'

    def run(self):
        print("Hello from release.py")

        # run test
        utils.msg('Running tests with `%s` command...\n' % (self.test_cmd))
        if not self.no_test:
            pypi_release.run_tests.run(self.test_cmd)

        # check next version
        self.version = utils.ask_next_version(self.version)
        print("next version: " + self.version)

        # update version strings in files
        #self.version_files の1個1個につき，前後3行くらい見せながら，y/nでupdateするかを確認していく
