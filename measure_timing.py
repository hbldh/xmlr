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
Time: 97.7521 s
xmller.xmlparse using xml.etree.cElementTree
Time: 46.4683 s
xmller.xmliter using xml.etree.ElementTree
Time: 98.0409 s
xmller.xmliter using xml.etree.cElementTree
Time: 98.3135 s
"""

n = 3

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
