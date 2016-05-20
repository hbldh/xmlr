#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`test_methods`
==================

Created by hbldh <henrik.blidh@nedomkull.com>
Created on 2016-05-20

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import


from xmller import XMLParsingMethods


def test_c_elementtree_available():
    assert XMLParsingMethods.cElementTree_available


def test_lxml_available():
    assert XMLParsingMethods.cElementTree_available
