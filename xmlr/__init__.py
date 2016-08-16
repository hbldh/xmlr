#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from .parse import xmlparse
from .iter import xmliter
from .methods import XMLParsingMethods

__all__ = ['xmlparse', 'xmliter', 'XMLParsingMethods']

# Version information.
__version__ = '0.3.1'
version = __version__  # backwards compatibility name
try:
    version_info = [int(x) if x.isdigit() else x for x in
                    re.match('^([0-9]+)\.([0-9]+)[\.]*([0-9]*)(.*)$',
                             __version__, re.DOTALL).groups()]
except Exception:
    version_info = ()

