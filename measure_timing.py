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
xmller.xmlparse using xml.etree.ElementTree
Time: 111.8283 s
xmller.xmlparse using xml.etree.cElementTree
Time: 51.4797 s
xmller.xmlparse using lxml.etree.ElementTree
Time: 51.7424 s
xmller.xmliter using xml.etree.ElementTree
Time: 111.4165 s
xmller.xmliter using xml.etree.cElementTree
Time: 51.1554 s
xmller.xmliter using lxml.etree.ElementTree
Time: 50.0234 s


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
t = timeit.timeit('xmlparse("/home/hbldh/Downloads/google-renewals-all-20080624.xml", False)', number=n, setup='from xmller import xmlparse')
print("Time: {0:.4f} s".format(t / n))

print ('xmller.xmlparse using xml.etree.cElementTree')
t = timeit.timeit('xmlparse("/home/hbldh/Downloads/google-renewals-all-20080624.xml", True)', number=n, setup='from xmller import xmlparse')
print("Time: {0:.4f} s".format(t / n))

print ('xmller.xmliter using xml.etree.ElementTree')
t = timeit.timeit('for d in xmliter("/home/hbldh/Downloads/google-renewals-all-20080624.xml", "Record", False): docs.append(d)',
                  number=n, setup='from xmller import xmliter; docs = []')
print("Time: {0:.4f} s".format(t / n))

print ('xmller.xmliter using xml.etree.cElementTree')
t = timeit.timeit('for d in xmliter("/home/hbldh/Downloads/google-renewals-all-20080624.xml", "Record", True): docs.append(d)',
                  number=n, setup='from xmller import xmliter; docs = []')
print("Time: {0:.4f} s\n".format(t / n))
