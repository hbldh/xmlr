# xmller

[![Build Status](https://travis-ci.org/hbldh/xmller.svg?branch=master)](https://travis-ci.org/hbldh/xmller)
[![Coverage Status](https://coveralls.io/repos/github/hbldh/xmller/badge.svg?branch=master)](https://coveralls.io/github/hbldh/xmller?branch=master)

Large XML files (>> 10 MB) are problematic to handle. Using the `xml` module 
in Python directly leads to huge memory overheads. Most often, these large XML 
files are pure data files, storing highly structured data that have no 
intrinsic need to be stored in XML.

This package provides iterative methods for dealing with them, reading the 
XML documents into Python dict representation instead, according to the 
methodology specified in \[3\]. `xmller` is inspired by the
solutions described in \[1\] and \[2\], enabling the parsing of very 
large documents without problems with overtaxing the memory. 

#### Notes

   This package generally provides a one way trip; there is not necessarily a 
   bijectional relation with the XML source after parsing.


## Installation

```
pip install git+https://www.github.com/hbldh/xmller
```

## Usage

To parse an entire document, use the `xmlparse` method:

```python
from xmller import xmlparse

doc = xmlparse('very_large_doc.xml')

```

An iterator, `xmliter`, yielding elements of a specified type as they are parsed from
the document is also present:

```python
from xmller import xmliter

for d in xmliter('very_large_record.xml', 'Record'):
    print(d)

```

The desired parser can also be specified. Available methods are:

- `ELEMENTTREE` - Using the `xml.etree.ElementTree` solution.
- `C_ELEMENTTREE` - Using the `xml.etree.cElementTree` solution.
- `LXML_ELEMENTTREE` - Using the `lxml.etree` solution. Requires 
  installation of the `lxml` package.

```python
from xmller import xmliter, XMLParsingMethods

for d in xmliter('very_large_record.xml', 'Record', 
        parser=XMLParsingMethods.ELEMENTTREE):
    print(d)

```

No type conversion is performed right now. A value in the output dictionary
can have the type `dict` (a subdocument), `list` (an array of similar 
documents), `str` (a leaf or value) or `None` (empty XML leaf tag). All keys
are of the type `str`.

## References

1. [High-performance XML parsing in Python with lxml](https://www.ibm.com/developerworks/xml/library/x-hiperfparse/)
2. [Parsing large XML files, serially, in Python](http://boscoh.com/programming/reading-xml-serially.html)
3. [Converting Between XML and JSON](http://www.xml.com/lpt/a/1658)

