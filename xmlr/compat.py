#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
xmlr.compat
~~~~~~~~~~~~~~

xmlr compatiblity module.

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import sys

is_py3 = (sys.version_info[0] > 2)


if is_py3:
    # py3 mappings
    unicode = str
    basestring = str
    xrange = range
