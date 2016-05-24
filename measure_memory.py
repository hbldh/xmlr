#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`timeit`
=======================

.. moduleauthor:: hbldh <henrik.blidh@swedwise.com>
Created on 2016-05-20, 13:28

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import os
from xmlr import xmlparse, xmliter, XMLParsingMethods


def document_size(doc):
    """A storage size estimator.

    :param doc: The document or list of documents to find size of.
    :type doc: dict or list
    :return: The size of the input document(s) in bytes.
    :rtype: int

    """
    import sys
    import datetime

    size = 0

    if isinstance(doc, (list, tuple)):
        # Add the base size the list or tuple.
        size += sys.getsizeof(type(doc)())
        # Iterate over all elements and sum their sizes.
        size += int(sum([document_size(d) for d in doc]))
    elif isinstance(doc, dict):
        # Add the base size of a dict.
        size += sys.getsizeof(type(doc)())
        for k in doc:
            # Add size of key.
            size += document_size(k)
            # Add size of value of key.
            size += document_size(doc[k])
    elif isinstance(doc, (datetime.datetime, float, int, long, basestring)):
        # Base type which can be evaluated with sys.getsizeof.
        size += sys.getsizeof(doc)
    elif doc is None:
        pass
    else:
        raise ValueError("Unsizable object: {0}".format(type(doc)))

    return size


filepath = '/home/hbldh/Downloads/google-renewals-all-20080624.xml'


"""


"""

# xmlparse

print ('xmlr.xmlparse using xml.etree.ElementTree')
doc = xmlparse("/home/hbldh/Downloads/google-renewals-all-20080624.xml", XMLParsingMethods.ELEMENTTREE)
print('Size in MB: {0:.2f} MB'.format(document_size(doc)/1024./1024.))
del doc

print ('xmlr.xmlparse using xml.etree.cElementTree')
doc = xmlparse("/home/hbldh/Downloads/google-renewals-all-20080624.xml", XMLParsingMethods.C_ELEMENTTREE)
print('Size in MB: {0:.2f} MB'.format(document_size(doc)/1024./1024.))
del doc

# print ('xmlr.xmlparse using lxml.etree')
# doc = xmlparse("/home/hbldh/Downloads/google-renewals-all-20080624.xml", XMLParsingMethods.LXML_ELEMENTTREE)
# print('Size in MB: {0:.2f} MB'.format(document_size(doc)/1024./1024.))
# del doc
#
# # xmliter
#
# print ('xmlr.xmliter using xml.etree.ElementTree')
# docs = []
# for d in xmliter("/home/hbldh/Downloads/google-renewals-all-20080624.xml", "Record", XMLParsingMethods.ELEMENTTREE):
#     docs.append(d)
# print('Size in MB: {0:.2f} MB'.format(document_size(docs)/1024./1024.))
# del docs
#
# print ('xmlr.xmliter using xml.etree.cElementTree')
# docs = []
# for d in xmliter("/home/hbldh/Downloads/google-renewals-all-20080624.xml", "Record", XMLParsingMethods.C_ELEMENTTREE):
#     docs.append(d)
# print('Size in MB: {0:.2f} MB'.format(document_size(docs)/1024./1024.))
# del docs
#
# print ('xmlr.xmliter using lxml.etree')
# docs = []
# for d in xmliter("/home/hbldh/Downloads/google-renewals-all-20080624.xml", "Record", XMLParsingMethods.LXML_ELEMENTTREE):
#     docs.append(d)
# print('Size in MB: {0:.2f} MB'.format(document_size(docs)/1024./1024.))
# del docs

# Straight parsing

#print ('lxml.parse')
#import lxml.etree as etree
#doc = etree.parse("/home/hbldh/Downloads/google-renewals-all-20080624.xml")

