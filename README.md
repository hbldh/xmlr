# XMeller

[![Build Status](https://travis-ci.org/hbldh/xmeller.svg?branch=master)](https://travis-ci.org/hbldh/xmeller)
[![Coverage Status](https://coveralls.io/repos/github/hbldh/xmeller/badge.svg?branch=master)](https://coveralls.io/github/hbldh/xmeller?branch=master)

An agnostic XML library, reading XML documents into 
Python dict representation. The agnostic part of it is this library provides
a one way trip; there is no bijectional relation with the XML source 
after parsing.
 
**XMeller** also uses an iterative handling of XML documents, inspired by the
solutions described in \[1\] and \[2\], enabling the parsing of very 
large documents (~1 GB) without problems with overtaxing the memory.

> Note that this is MUCH slower than performing a regular 
> `xml.etree.ElementTree.parse` and that is by design!

## Installation

```
pip install git+https://www.github.com/hbldh/xmeller
```

## Usage
 
```python
from xmeller import xmlparse

doc = xmlparse('very_large_doc.xml')

```

No type conversion is performed right now. A field in the output dictionary
can have the type `dict` (a subdocument), `list` (an array of similar 
documents), `str` (a leaf or value) or `None` (empty XML leaf tag).

## References

1. [High-performance XML parsing in Python with lxml](https://www.ibm.com/developerworks/xml/library/x-hiperfparse/)
2. [Parsing large XML files, serially, in Python](http://boscoh.com/programming/reading-xml-serially.html)
3. [Converting Between XML and JSON](http://www.xml.com/lpt/a/1658)

