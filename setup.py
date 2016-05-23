# -*- coding: utf-8 -*-
"""
:mod:`setup.py`
===============

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>
Created on 2015-11-05

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import sys
import re
from codecs import open
from setuptools import setup, find_packages


basedir = os.path.dirname(os.path.abspath(__file__))

if sys.argv[-1] == 'publish':
    os.system('python setup.py register')
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()


def read(f):
    return open(f, encoding='utf-8').read()

with open('xmlr/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)


setup(
    name='xmlr',
    version=version,
    author='Henrik Blidh',
    author_email='henrik.blidh@nedomkull.com',
    url='https://github.com/hbldh/xmlr',
    description='XML parsing package for very large files',
    long_description=read('README.rst') + '\n\n' + read('HISTORY.rst'),
    license='MIT',
    keywords=['XML', 'parsing', 'json', 'conversion'],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Markup :: XML'
    ],
    packages=find_packages(exclude=['tests', 'docs']),
    test_suite="tests",
    dependency_links=[],
    entry_points={},
)

