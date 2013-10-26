# -*- coding: utf-8 -*-
from nose.tools import *
import os
from pypi_release.versions import get_current_version


ORIGIN_DIR     = os.path.abspath(os.getcwd())
SAMPLE_PKG_DIR = ORIGIN_DIR + '/pypi_release/test/sample_pkg_ver2.5.6'


def setup():
    os.chdir(SAMPLE_PKG_DIR)


def teardown():
    print(ORIGIN_DIR)


def test_get_current_version():
    eq_(get_current_version(), 'ver2.5.6')
