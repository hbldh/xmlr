#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
xmlr.methods
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
    LET = CET if _cet_available else ET
    _let_available = False


class XMLParsingMethods(object):
    """Enum facsimile to simplify using different XML parsing backends.

    Contains the following element tree references:

    - `ELEMENTTREE` - Using the `xml.etree.ElementTree` solution.
    - `C_ELEMENTTREE` - Using the `xml.etree.cElementTree` solution.
    - `LXML_ELEMENTTREE` - Using the `lxml.etree` solution. Requires
      installation of the `lxml` package.

    .. code:: python

        from xmlr import xmliter, XMLParsingMethods

        for d in xmliter('very_large_record.xml', 'Record',
                parser=XMLParsingMethods.LXML_ELEMENTTREE):
            print(d)

    If the desired method is unavailable, fallback is in the order described
    in the listing above.

    There are two attributes of this class that can be used to test if the
    different backends are available in the current Python environment:

    .. code:: python

        In [1]: from xmlr import XMLParsingMethods

        In [2]: XMLParsingMethods.cElementTree_available
        Out[2]: True

        In [3]: XMLParsingMethods.lxml_available
        Out[3]: False

    """
    ELEMENTTREE = ET
    C_ELEMENTTREE = CET
    LXML_ELEMENTTREE = LET

    cElementTree_available = _cet_available
    lxml_available = _let_available
