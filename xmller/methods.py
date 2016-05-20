#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
xmller.methods
~~~~~~~~~~~~~~

:copyright: 2016 by Henrik Blidh <henrik.blidh@nedomkull.com>

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from xml.etree import ElementTree as ET

try:
    from xml.etree import cElementTree as CET
    _cet_available = True
except ImportError:
    CET = ET
    _cet_available = False

try:
    from lxml import etree as LET
    _let_available = True
except ImportError:
    LET = ET
    _let_available = False


class XMLParsingMethods(object):
    ELEMENTTREE = ET
    C_ELEMENTTREE = CET
    LXML_ELEMENTTREE = LET

    _cet_available = _cet_available
    _let_available = _let_available

    @property
    def cElementTree_available(self):
        return self._cet_available

    @property
    def lxml_available(self):
        return self._let_available
