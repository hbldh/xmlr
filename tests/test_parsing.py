#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`test_parsing`
=======================

.. moduleauthor:: hbldh <henrik.blidh@swedwise.com>
Created on 2016-05-17, 14:01

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os
import sys
import tempfile
from xml.etree.ElementTree import ParseError

import pytest

from xmeller import xmlparse
from xmeller.compat import *

if sys.version_info[0] > 2:
    from urllib.request import urlopen
else:
    from urllib2 import urlopen

_note_url = 'http://www.w3schools.com/xml/note.xml'
_note_with_error_url = 'http://www.w3schools.com/xml/note_error.xml'
_cd_catalog_url = 'http://www.w3schools.com/xml/cd_catalog.xml'
_plant_catalog_url = 'http://www.w3schools.com/xml/plant_catalog.xml'
_menu_url = 'http://www.w3schools.com/xml/simple.xml'


@pytest.fixture(scope='module', params=[_note_url,
                                        _note_with_error_url,
                                        _cd_catalog_url,
                                        _plant_catalog_url,
                                        _menu_url],
                ids=['note', 'note_error', 'cd', 'plant', 'menu'])
def xmldata(request):
    with tempfile.NamedTemporaryFile(prefix='xmeller_', suffix='.xml', delete=False) as f:
        f.write(urlopen(request.param).read())
        f.flush()

    def fin():
        try:
            os.remove(f.name)
        except:
            pass
    request.addfinalizer(fin)

    return f.name, request.param == _note_with_error_url


def test_parsing(xmldata):

    xmlfile, is_error = xmldata
    if is_error:
        with pytest.raises(ParseError):
            xmlparse(xmlfile)
    else:
        doc = xmlparse(xmlfile)

        def walk_test(node):
            for key, dict_item in node.items():
                if isinstance(dict_item, dict):
                    walk_test(dict_item)
                elif isinstance(dict_item, list):
                    for list_item in dict_item:
                        if isinstance(list_item, dict):
                            walk_test(list_item)
                        else:
                            assert isinstance(list_item, basestring) or \
                                   list_item is None
                else:
                    assert isinstance(dict_item, basestring) or \
                           list_item is None

        assert isinstance(doc, dict)
        walk_test(doc)


