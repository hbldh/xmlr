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


import timeit


"""
Python 2.7
--------

xmller.xmlparse using xml.etree.ElementTree
Time: 114.6762 s
xmller.xmlparse using xml.etree.cElementTree
Time: 51.9837 s
xmller.xmlparse using lxml.etree
Time: 53.6425 s
xmller.xmliter using xml.etree.ElementTree
Time: 117.9564 s
xmller.xmliter using xml.etree.cElementTree
Time: 60.8914 s
xmller.xmliter using lxml.etree
Time: 48.2994 s


Python 3.5
--------

xmller.xmlparse using xml.etree.ElementTree
Time: 73.2584 s
xmller.xmlparse using xml.etree.cElementTree
Time: 72.6901 s
xmller.xmlparse using lxml.etree
Time: 53.3402 s
xmller.xmliter using xml.etree.ElementTree
Time: 71.5361 s
xmller.xmliter using xml.etree.cElementTree
Time: 72.6967 s
xmller.xmliter using lxml.etree
Time: 48.9455 s


PyPy
----

xmller.xmlparse using xml.etree.ElementTree
Time: 42.3088 s
xmller.xmlparse using xml.etree.cElementTree
Time: 43.0353 s
xmller.xmlparse using lxml.etree
Time: 538.7466 s
xmller.xmliter using xml.etree.ElementTree
Time: 42.5941 s
xmller.xmliter using xml.etree.cElementTree
Time: 42.3841 s
xmller.xmliter using lxml.etree
Time: 271.5306 s


"""

n = 1

# xmlparse

print ('xmller.xmlparse using xml.etree.ElementTree')
t = timeit.timeit('xmlparse("/home/hbldh/Downloads/google-renewals-all-20080624.xml", XMLParsingMethods.ELEMENTTREE)', number=n, setup='from xmller import xmlparse, XMLParsingMethods')
print("Time: {0:.4f} s".format(t / n))

print ('xmller.xmlparse using xml.etree.cElementTree')
t = timeit.timeit('xmlparse("/home/hbldh/Downloads/google-renewals-all-20080624.xml", XMLParsingMethods.C_ELEMENTTREE)', number=n, setup='from xmller import xmlparse, XMLParsingMethods')
print("Time: {0:.4f} s".format(t / n))

print ('xmller.xmlparse using lxml.etree')
t = timeit.timeit('xmlparse("/home/hbldh/Downloads/google-renewals-all-20080624.xml", XMLParsingMethods.LXML_ELEMENTTREE)', number=n, setup='from xmller import xmlparse, XMLParsingMethods')
print("Time: {0:.4f} s".format(t / n))

# xmliter

print ('xmller.xmliter using xml.etree.ElementTree')
t = timeit.timeit('for d in xmliter("/home/hbldh/Downloads/google-renewals-all-20080624.xml", "Record", XMLParsingMethods.ELEMENTTREE): docs.append(d)',
                  number=n, setup='from xmller import xmliter, XMLParsingMethods; docs = []')
print("Time: {0:.4f} s".format(t / n))

print ('xmller.xmliter using xml.etree.cElementTree')
t = timeit.timeit('for d in xmliter("/home/hbldh/Downloads/google-renewals-all-20080624.xml", "Record", XMLParsingMethods.C_ELEMENTTREE): docs.append(d)',
                  number=n, setup='from xmller import xmliter, XMLParsingMethods; docs = []')
print("Time: {0:.4f} s".format(t / n))

print ('xmller.xmliter using lxml.etree')
t = timeit.timeit('for d in xmliter("/home/hbldh/Downloads/google-renewals-all-20080624.xml", "Record", XMLParsingMethods.LXML_ELEMENTTREE): docs.append(d)',
                  number=n, setup='from xmller import xmliter, XMLParsingMethods; docs = []')
print("Time: {0:.4f} s".format(t / n))
