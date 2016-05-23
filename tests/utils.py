#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`fixtures`
=======================

.. moduleauthor:: hbldh <henrik.blidh@swedwise.com>
Created on 2016-05-20, 15:48

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import


import os
import sys
import tempfile

import pytest

from xmlr.compat import *

if sys.version_info[0] > 2:
    from urllib.request import urlopen
else:
    from urllib2 import urlopen

_note_url = 'http://www.w3schools.com/xml/note.xml'
_note_with_error_url = 'http://www.w3schools.com/xml/note_error.xml'
_cd_catalog_url = 'http://www.w3schools.com/xml/cd_catalog.xml'
_plant_catalog_url = 'http://www.w3schools.com/xml/plant_catalog.xml'
_menu_url = 'http://www.w3schools.com/xml/simple.xml'


@pytest.fixture(scope='module')
def xmldata_note(request):
    with tempfile.NamedTemporaryFile(prefix='xmller_', suffix='.xml',
                                     delete=False) as f:
        f.write(urlopen(_note_url).read())
        f.flush()

    def fin():
        try:
            os.remove(f.name)
        except:
            pass

    request.addfinalizer(fin)

    return f.name


@pytest.fixture(scope='module')
def xmldata_note_error(request):
    with tempfile.NamedTemporaryFile(prefix='xmller_', suffix='.xml',
                                     delete=False) as f:
        f.write(urlopen(_note_with_error_url).read())
        f.flush()

    def fin():
        try:
            os.remove(f.name)
        except:
            pass

    request.addfinalizer(fin)

    return f.name


@pytest.fixture(scope='module')
def xmldata_cd(request):
    with tempfile.NamedTemporaryFile(prefix='xmller_', suffix='.xml',
                                     delete=False) as f:
        f.write(urlopen(_cd_catalog_url).read())
        f.flush()

    def fin():
        try:
            os.remove(f.name)
        except:
            pass

    request.addfinalizer(fin)

    return f.name


@pytest.fixture(scope='module')
def xmldata_plants(request):
    with tempfile.NamedTemporaryFile(prefix='xmller_', suffix='.xml',
                                     delete=False) as f:
        f.write(urlopen(_plant_catalog_url).read())
        f.flush()

    def fin():
        try:
            os.remove(f.name)
        except:
            pass

    request.addfinalizer(fin)

    return f.name


@pytest.fixture(scope='module')
def xmldata_menu(request):
    with tempfile.NamedTemporaryFile(prefix='xmller_', suffix='.xml',
                                     delete=False) as f:
        f.write(urlopen(_menu_url).read())
        f.flush()

    def fin():
        try:
            os.remove(f.name)
        except:
            pass

    request.addfinalizer(fin)

    return f.name


def walk_test(node):
    for key, dict_item in node.items():
        assert isinstance(key, unicode)
        if isinstance(dict_item, dict):
            walk_test(dict_item)
        elif isinstance(dict_item, list):
            for list_item in dict_item:
                if isinstance(list_item, dict):
                    walk_test(list_item)
                else:
                    assert isinstance(list_item, unicode) or list_item is None
        else:
            assert isinstance(dict_item, unicode) or dict_item is None
