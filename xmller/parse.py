#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
xmller.parse
~~~~~~~~~~~~~

:copyright: 2016 by Henrik Blidh <henrik.blidh@nedomkull.com>

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from operator import setitem

import xml.etree.ElementTree as etree

from xmller.compat import *


def xmlparse(document_path):

    iterparser = etree.iterparse(
        document_path, events=('start', 'end'))

    output = {}
    current_position = []
    current_index = []

    for event, elem in iterparser:
        if event == 'start':
            tmp = output
            for cp, ci in zip(current_position, current_index):
                tmp = tmp[cp]
                if ci:
                    tmp = tmp[ci]

            if elem.tag not in tmp:
                tmp[elem.tag] = {}
                current_index.append(None)
            else:
                if isinstance(tmp[elem.tag], list):
                    current_index.append(len(tmp[elem.tag]))
                    tmp[elem.tag].append({})
                else:
                    tmp[elem.tag] = [tmp[elem.tag], {}]
                    current_index.append(1)
            current_position.append(elem.tag)
        elif event == 'end':
            tmp = output
            for cp, ci in zip(current_position[:-1], current_index[:-1]):
                tmp = tmp[cp]
                if ci:
                    tmp = tmp[ci]

            attribs = elem.attrib

            cp = current_position[-1]
            ci = current_index[-1]

            if ci:
                setfcn = lambda x: setitem(tmp[cp], ci, x)
                tmp[cp][ci].update(attribs.copy())
            else:
                setfcn = lambda x: setitem(tmp, cp, x)
                tmp[cp].update(attribs.copy())

            if elem.text and elem.text.strip():
                setfcn({'#text': elem.text.strip()})

            if ci:
                if tmp[cp][ci]:
                    nk = len(tmp[cp][ci].keys())
                    if nk == 1 and "#text" in tmp[cp][ci]:
                        tmp[cp][ci] = tmp[cp][ci]["#text"]
                    elif nk == 0:
                        tmp[cp][ci] = None
                else:
                    tmp[cp][ci] = None
            else:
                nk = len(tmp[cp].keys())
                if nk == 1 and "#text" in tmp[cp]:
                    tmp[cp] = tmp[cp]["#text"]
                elif nk == 0:
                    tmp[cp] = None

            current_position.pop()
            current_index.pop()

            elem.clear()
        else:
            print(event)

    return output


def main():
    import os

    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
        'data', 'google-renewals-all-20080624.xml')

    doc = xmlparse(filepath)


if __name__ == "__main__":
    main()
