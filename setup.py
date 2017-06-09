#!/usr/bin/env python3
"""
Hexdump Utility
===============

A command line hexdump utility.

See the module's `Github homepage <https://github.com/dmulholland/hex>`_
for details.

"""

import os
import re
import io

from setuptools import setup


filepath = os.path.join(os.path.dirname(__file__), 'hex.py')
with io.open(filepath, encoding='utf-8') as metafile:
    regex = r'''^__([a-z]+)__ = ["'](.*)["']'''
    meta = dict(re.findall(regex, metafile.read(), flags=re.MULTILINE))


setup(
    name = 'hex',
    version = meta['version'],
    py_modules = ['hex'],
    entry_points = {
        'console_scripts': [
            'hex = hex:main',
        ],
    },
    author = 'Darren Mulholland',
    url = 'https://github.com/dmulholland/hex',
    license = 'Public Domain',
    description = (
        'Hexdump command line utility.'
    ),
    long_description = __doc__,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: Public Domain',
        'Topic :: Utilities',
    ],
)
