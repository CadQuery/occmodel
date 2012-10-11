#!/usr/bin/python2
# -*- coding: utf-8 -*-
# This is code is commercial software.
# Copyright 2007 by Runar Tenfjord, Tenko.
import sys
import os

from distutils.core import setup
from sphinx.setup_command import BuildDoc
cmdclass = {'build_sphinx': BuildDoc}

name = 'occmodel'
version = '0.1'
release = '0.1.0'

try:
    setup(
        name=name,
        author='Runar Tenfjord',
        version=release,
        cmdclass=cmdclass,
        command_options={
            'build_sphinx': {
               'builder': ('setup_docs.py', 'html'),
               }
        },
                   
    )
except:
    print('Traceback\n:%s\n' % str(sys.exc_info()[-2]))
    sys.exit(1)
else:
    print('\n')