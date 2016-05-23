#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
xmlr.parse
~~~~~~~~~~~~~

:copyright: 2016 by Henrik Blidh <henrik.blidh@nedomkull.com>

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from operator import setitem

from .methods import XMLParsingMethods
from .compat import *


def xmlparse(source, parsing_method=XMLParsingMethods.C_ELEMENTTREE, **kwargs):
    """Parses a XML document into a dictionary.

    Details about how the XML is converted into this dictionary (json)
    representation is described in reference [3] in the README.

    :param str,file-like source: Either the path to a XML document to parse
        or a file-like object (with `read` attribute) containing an XML.
    :param parsing_method: ElementTree implementation.
        See :py:mod:`xmlr.methods`. Uses the
        :py:class:`xml.etree.cElementTree` as default.
    :return: The parsed XML in dictionary representation.
    :rtype: dict

    """
    if parsing_method.__name__.startswith('lxml'):
        _is_lxml = True
    else:
        _is_lxml = False

    # This is the output dict.
    output = {}

    # Keeping track of the depth and position to store data in.
    current_position = []
    current_index = []

    # Start iterating over the Element Tree.
    for event, elem in parsing_method.iterparse(
            source, events=(str('start'), str('end')), **kwargs):
        if event == 'start':
            # Start of new tag.

            # Extract the current endpoint so add the new element to it.
            tmp = output
            for cp, ci in zip(current_position, current_index):
                tmp = tmp[cp]
                if ci:
                    tmp = tmp[ci]

            this_tag_name = unicode(elem.tag)
            # If it is a previously unseen tag, create a new key and
            # stick an empty dict there. Set index of this level to None.
            if this_tag_name not in tmp:
                tmp[this_tag_name] = {}
                current_index.append(None)
            else:
                # The tag name already exists. This means that we have to change
                # the value of this element's key to a list if this hasn't
                # been done already and add an empty dict to the end of that
                # list. If it already is a list, just add an new dict and update
                # the current index.
                if isinstance(tmp[this_tag_name], list):
                    current_index.append(len(tmp[this_tag_name]))
                    tmp[this_tag_name].append({})
                else:
                    tmp[this_tag_name] = [tmp[this_tag_name], {}]
                    current_index.append(1)

            # Set the position of the iteration to this element's tag name.
            current_position.append(this_tag_name)
        elif event == 'end':
            # End of a tag.

            # Extract the current endpoint's parent so we can handle
            # the endpoint's data by reference.
            tmp = output
            for cp, ci in zip(current_position[:-1], current_index[:-1]):
                tmp = tmp[cp]
                if ci:
                    tmp = tmp[ci]
            cp = current_position[-1]
            ci = current_index[-1]

            # If this current endpoint is a dict in a list or not has
            # implications on how to set data.
            if ci:
                setfcn = lambda x: setitem(tmp[cp], ci, x)
                for attr_name, attr_value in elem.attrib.items():
                    tmp[cp][ci]["@{0}".format(attr_name)] = unicode(attr_value)
            else:
                setfcn = lambda x: setitem(tmp, cp, x)
                for attr_name, attr_value in elem.attrib.items():
                    tmp[cp]["@{0}".format(attr_name)] = unicode(attr_value)

            # If there is any text in the tag, add it here.
            if elem.text and elem.text.strip():
                setfcn({'#text': unicode(elem.text.strip())})

            # Handle special cases:
            # 1) when the tag only harbours text, replace the dict content with
            #    that very text string.
            # 2) when no text, attributes or children are present, content
            #    is set to None
            # These are detailed in reference [3] in README.
            if ci:
                nk = len(tmp[cp][ci].keys())
                if nk == 1 and "#text" in tmp[cp][ci]:
                    tmp[cp][ci] = tmp[cp][ci]["#text"]
                elif nk == 0:
                    tmp[cp][ci] = None
            else:
                nk = len(tmp[cp].keys())
                if nk == 1 and "#text" in tmp[cp]:
                    tmp[cp] = tmp[cp]["#text"]
                elif nk == 0:
                    tmp[cp] = None

            # Remove the outermost position and index, since we just finished
            # handling that element.
            current_position.pop()
            current_index.pop()

            # Most important of all, release the element's memory allocations
            # so we actually benefit from the iterative processing!
            elem.clear()
            if _is_lxml:
                while elem.getprevious() is not None:
                    del elem.getparent()[0]

    return output
