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
from xmller import xmlparse, xmliter

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
        size += int(sum([document_size(d) for d in doc]))
    elif isinstance(doc, dict):
        for k in doc:
            size += document_size(doc[k])
    elif isinstance(doc, (datetime.datetime, float, int, long, basestring)):
        size += sys.getsizeof(doc)
    elif doc is None:
        pass
    else:
        raise ValueError("Unsizable object: {0}".format(type(doc)))

    return size


filepath = '/home/hbldh/Downloads/google-renewals-all-20080624.xml'

doc = xmlparse(filepath)
#for d in xmliter(filepath, 'Record'):
#    pass

#print('Size in MB: {0:.2f} MB'.format(document_size(doc)/1024./1024.))



import timeit

"""
xmller.xmlparse using xml.etree.ElementTree
Time: 111.8283 s
xmller.xmlparse using xml.etree.cElementTree
Time: 51.4797 s
xmller.xmliter using xml.etree.ElementTree
Time: 111.4165 s
xmller.xmliter using xml.etree.cElementTree
Time: 51.1554 s


PyPy
----

xmller.xmlparse using xml.etree.ElementTree
Time: 39.7572 s
xmller.xmlparse using xml.etree.cElementTree
Time: 39.0134 s
xmller.xmliter using xml.etree.ElementTree
Time: 39.7219 s
xmller.xmliter using xml.etree.cElementTree
Time: 38.9378 s



"""

n = 1

print ('xmller.xmlparse using xml.etree.ElementTree')
doc = xmlparse("/home/hbldh/Downloads/google-renewals-all-20080624.xml", False)
del doc

print ('xmller.xmlparse using xml.etree.cElementTree')
doc = xmlparse("/home/hbldh/Downloads/google-renewals-all-20080624.xml", True)
del doc

print ('xmller.xmliter using xml.etree.ElementTree')
docs = []
for d in xmliter("/home/hbldh/Downloads/google-renewals-all-20080624.xml", "Record", False):
    docs.append(d)
del docs

print ('xmller.xmliter using xml.etree.cElementTree')
docs = []
for d in xmliter("/home/hbldh/Downloads/google-renewals-all-20080624.xml", "Record", True):
    docs.append(d)
del docs

print ('lxml.parse')
import lxml.etree as etree
doc = etree.parse("/home/hbldh/Downloads/google-renewals-all-20080624.xml")

