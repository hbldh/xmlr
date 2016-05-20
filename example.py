#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
example
~~~~~~~

:copyright: 2016 by Henrik Blidh <henrik.blidh@nedomkull.com>

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


"""
/home/hbldh/.virtualenvs/xmlr/bin/python /home/hbldh/Repos/xmller/example.py
Timer unit: 1e-06 s

Total time: 617.28 s
File: /home/hbldh/Repos/xmller/xmller/parse.py
Function: xmlparse at line 24

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    24                                           @do_profile(follow=[])
    25                                           def xmlparse(source):
    26                                               "Parses a XML document into a dictionary.
    27
    28                                               Details about how the XML is converted into this dictionary (json)
    29                                               representation is described in reference [3] in the README.
    30
    31                                               :param str,file-like source: Either the path to a XML document to parse
    32                                                   or a file-like object (with `read` attribute) containing an XML.
    33                                               :return: The parsed XML in dictionary representation.
    34                                               :rtype: dict
    35
    36                                               "
    37
    38                                               # This is the output dict.
    39         1            2      2.0      0.0      output = {}
    40
    41                                               # Keeping track of the depth and position to store data in.
    42         1            2      2.0      0.0      current_position = []
    43         1            1      1.0      0.0      current_index = []
    44
    45                                               # Start iterating over the Element Tree.
    46  20002755    274219269     13.7     44.4      for event, elem in etree.iterparse(source, events=('start', 'end')):
    47
    48  20002754     14338962      0.7      2.3          if event == 'start':
    49                                                       # Start of new tag.
    50
    51                                                       # Extract the current endpoint so add the new element to it.
    52  10001377      6518098      0.7      1.1              tmp = output
    53  33354063     31370018      0.9      5.1              for cp, ci in zip(current_position, current_index):
    54  23352686     16696923      0.7      2.7                  tmp = tmp[cp]
    55  23352686     15522914      0.7      2.5                  if ci:
    56  10125234      6999403      0.7      1.1                      tmp = tmp[ci]
    57
    58                                                       # If it is a previously unseen tag, create a new key and
    59                                                       # stick an empty dict there. Set index of this level to None.
    60  10001377      9180952      0.9      1.5              if elem.tag not in tmp:
    61   9288601      7656359      0.8      1.2                  tmp[elem.tag] = {}
    62   9288601      7191787      0.8      1.2                  current_index.append(None)
    63                                                       else:
    64                                                           # The tag name already exists. This means that we have to change
    65                                                           # the value of this element's key to a list if this hasn't
    66                                                           # been done already and add an empty dict to the end of that
    67                                                           # list. If it already is a list, just add an new dict and update
    68                                                           # the current index.
    69    712776       877547      1.2      0.1                  if isinstance(tmp[elem.tag], list):
    70    538025       511365      1.0      0.1                      current_index.append(len(tmp[elem.tag]))
    71    538025       519911      1.0      0.1                      tmp[elem.tag].append({})
    72                                                           else:
    73    174751       187883      1.1      0.0                      tmp[elem.tag] = [tmp[elem.tag], {}]
    74    174751       139209      0.8      0.0                      current_index.append(1)
    75
    76                                                       # Set the position of the iteration to this element's tag name.
    77  10001377      7662965      0.8      1.2              current_position.append(elem.tag)
    78  10001377      6892039      0.7      1.1          elif event == 'end':
    79                                                       # End of a tag.
    80
    81                                                       # Extract the current endpoint's parent so we can handle
    82                                                       # the endpoint's data by reference.
    83  10001377      6864769      0.7      1.1              tmp = output
    84  33354063     31561119      0.9      5.1              for cp, ci in zip(current_position[:-1], current_index[:-1]):
    85  23352686     16642736      0.7      2.7                  tmp = tmp[cp]
    86  23352686     16027043      0.7      2.6                  if ci:
    87  10125234      7210423      0.7      1.2                      tmp = tmp[ci]
    88  10001377      7366523      0.7      1.2              cp = current_position[-1]
    89  10001377      7136424      0.7      1.2              ci = current_index[-1]
    90
    91                                                       # If this current endpoint is a dict in a list or not has
    92                                                       # implications on how to set data.
    93  10001377      7074298      0.7      1.1              if ci:
    94    712776       616493      0.9      0.1                  setfcn = lambda x: setitem(tmp[cp], ci, x)
    95    712776       841608      1.2      0.1                  for attr_name, attr_value in elem.attrib.items():
    96                                                               tmp[cp][ci]["@{0}".format(attr_name)] = attr_value
    97                                                       else:
    98   9288601      7738505      0.8      1.3                  setfcn = lambda x: setitem(tmp, cp, x)
    99   9288601     10371346      1.1      1.7                  for attr_name, attr_value in elem.attrib.items():
   100                                                               tmp[cp]["@{0}".format(attr_name)] = attr_value
   101
   102                                                       # If there is any text in the tag, add it here.
   103  10001377     10404082      1.0      1.7              if elem.text and elem.text.strip():
   104   7236956     10537021      1.5      1.7                  setfcn({'#text': elem.text.strip()})
   105
   106                                                       # Handle special cases:
   107                                                       # 1) when the tag only harbours text, replace the dict content with
   108                                                       #    that very text string.
   109                                                       # 2) when no text, attributes or children are present, content
   110                                                       #    is set to None
   111                                                       # These are detailed in reference [3] in README.
   112  10001377      7151849      0.7      1.2              if ci:
   113    712776       585150      0.8      0.1                  if tmp[cp][ci]:
   114    712776       837771      1.2      0.1                      nk = len(tmp[cp][ci].keys())
   115    712776       547525      0.8      0.1                      if nk == 1 and "#text" in tmp[cp][ci]:
   116     10476        11350      1.1      0.0                          tmp[cp][ci] = tmp[cp][ci]["#text"]
   117    702300       555887      0.8      0.1                      elif nk == 0:
   118                                                                   tmp[cp][ci] = None
   119                                                           else:
   120                                                               tmp[cp][ci] = None
   121                                                       else:
   122   9288601      9208817      1.0      1.5                  nk = len(tmp[cp].keys())
   123   9288601      7820125      0.8      1.3                  if nk == 1 and "#text" in tmp[cp]:
   124   7226480      6302221      0.9      1.0                      tmp[cp] = tmp[cp]["#text"]
   125   2062121      1498068      0.7      0.2                  elif nk == 0:
   126    449301       359538      0.8      0.1                      tmp[cp] = None
   127
   128                                                       # Remove the outermost position and index, since we just finished
   129                                                       # handling that element.
   130  10001377      8614181      0.9      1.4              current_position.pop()
   131  10001377      7856807      0.8      1.3              current_index.pop()
   132
   133                                                       # Most important of all, release the element's memory allocations
   134                                                       # so we actually benefit from the iterative processing!
   135  10001377     19052512      1.9      3.1              elem.clear()
   136
   137         1            2      2.0      0.0      return output
"""
