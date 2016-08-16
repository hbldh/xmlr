xmlr
====

|Build Status| |Coverage Status|

It can be problematic to handle large XML files (>> 10 MB) and using the
``xml`` module in Python directly leads to huge memory overheads. Most
often, these large XML files are pure data files, storing highly
structured data that have no intrinsic need to be stored in XML.

This package provides iterative methods for dealing with them, reading
the XML documents into Python dict representation instead, according to
methodology specifed on the page `Converting Between XML and JSON
<http://www.xml.com/lpt/a/1658>`_. ``xmlr`` is inspired by the solutions
described in the blog posts `High-performance XML parsing in Python with lxml
<https://www.ibm.com/developerworks/xml/library/x-hiperfparse/>`_ and
`Parsing large XML files, serially, in Python
<http://boscoh.com/programming/reading-xml-serially.html>`_,
enabling the parsing of very large documents without problems with
overtaxing the memory.

.. pull-quote::

    This package generally provides a one way trip; there is not necessarily
    a bijectional relation with the XML source after parsing.

Installation
------------

::

    pip install xmlr

Usage
-----

To parse an entire document, use the ``xmlparse`` method:

.. code:: python

    from xmlr import xmlparse

    doc = xmlparse('very_large_doc.xml')

An iterator, ``xmliter``, yielding elements of a specified type as they
are parsed from the document is also present:

.. code:: python

    from xmlr import xmliter

    for d in xmliter('very_large_record.xml', 'Record'):
        print(d)

The desired parser can also be specified. Available methods are:

-  ``ELEMENTTREE`` - Using ``xml.etree.ElementTree`` as backend.
-  ``C_ELEMENTTREE`` - Using ``xml.etree.cElementTree`` as backend.
-  ``LXML_ELEMENTTREE`` - Using ``lxml.etree`` as backend. Requires
   installation of the ``lxml`` package.

These can then be used like this:

.. code:: python

    from xmlr import xmliter, XMLParsingMethods

    for d in xmliter('very_large_record.xml', 'Record', parser=XMLParsingMethods.LXML_ELEMENTTREE):
        print(d)

No type conversion is performed right now. A value in the output
dictionary can have the type ``dict`` (a subdocument), ``list`` (an
array of similar documents), ``str`` (a leaf or value) or ``None``
(empty XML leaf tag). All keys are of the type ``str``.

Tests
~~~~~

Tests are run with ``pytest``:

.. code:: bash

    $ py.test tests/
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.6, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
    rootdir: /home/hbldh/Repos/xmlr, inifile:
    collected 50 items

    tests/test_iter.py ...........................
    tests/test_methods.py ..
    tests/test_parsing.py .....................

    ========================== 50 passed in 0.50 seconds ===========================

The tests fetches some XML documents from `W3Schools XML tutorials`_ and
also uses a bundled, slimmed down version of the document available at
`U.S. copyright renewal records available for download
<http://booksearch.blogspot.se/2008/06/us-copyright-renewal-records-available.html>`_.


.. _W3Schools XML tutorials: http://www.w3schools.com/xml/xml_examples.asp

.. |Build Status| image:: https://travis-ci.org/hbldh/xmlr.svg?branch=master
   :target: https://travis-ci.org/hbldh/xmlr
.. |Coverage Status| image:: https://coveralls.io/repos/github/hbldh/xmlr/badge.svg?branch=master
   :target: https://coveralls.io/github/hbldh/xmlr?branch=master


