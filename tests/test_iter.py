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

from xml.etree.ElementTree import ParseError
from xml.etree.cElementTree import ParseError as cParseError
from lxml.etree import XMLSyntaxError

import pytest

from xmller import xmliter, XMLParsingMethods
from xmller.compat import *

from .fixtures import xmldata_note, xmldata_note_error, \
    xmldata_cd, xmldata_menu, xmldata_plants


@pytest.mark.parametrize("parser", (XMLParsingMethods.ELEMENTTREE,
                                    XMLParsingMethods.C_ELEMENTTREE,
                                    XMLParsingMethods.LXML_ELEMENTTREE))
def test_parsing_note(xmldata_note, parser):
    docs = []
    for doc in xmliter(xmldata_note, 'note', parsing_method=parser):
        assert isinstance(doc, dict)
        docs.append(doc)
    assert len(docs)


@pytest.mark.parametrize("parser", (XMLParsingMethods.ELEMENTTREE,
                                    XMLParsingMethods.C_ELEMENTTREE,
                                    XMLParsingMethods.LXML_ELEMENTTREE))
def test_parsing_note_error(xmldata_note_error, parser):
    with pytest.raises((ParseError, cParseError, XMLSyntaxError), parsing_method=parser):
        for doc in xmliter(xmldata_note_error, 'note', parsing_method=parser):
            pass


@pytest.mark.parametrize("parser", (XMLParsingMethods.ELEMENTTREE,
                                    XMLParsingMethods.C_ELEMENTTREE,
                                    XMLParsingMethods.LXML_ELEMENTTREE))
def test_parsing_cd(xmldata_cd, parser):
    docs = []
    for doc in xmliter(xmldata_cd, 'CD', parsing_method=parser):
        assert isinstance(doc, dict)
        docs.append(doc)
    assert len(docs) == 26


@pytest.mark.parametrize("parser", (XMLParsingMethods.ELEMENTTREE,
                                    XMLParsingMethods.C_ELEMENTTREE,
                                    XMLParsingMethods.LXML_ELEMENTTREE))
def test_parsing_plants(xmldata_plants, parser):
    docs = []
    for doc in xmliter(xmldata_plants, 'PLANT', parsing_method=parser):
        assert isinstance(doc, dict)
        docs.append(doc)
    assert len(docs) == 36


@pytest.mark.parametrize("parser", (XMLParsingMethods.ELEMENTTREE,
                                    XMLParsingMethods.C_ELEMENTTREE,
                                    XMLParsingMethods.LXML_ELEMENTTREE))
def test_parsing_menu(xmldata_menu, parser):
    docs = []
    for doc in xmliter(xmldata_menu, 'food', parsing_method=parser):
        assert isinstance(doc, dict)
        docs.append(doc)
    assert len(docs) == 5



