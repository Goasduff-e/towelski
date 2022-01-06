#!/usr/bin/python
# -*- coding: utf-8 -*-
#Julien>Erwann

import os
from setuptools import setup
from setuptools import find_packages
# this is only necessary when not using setuptools/distribute
from flask.setup_command import BuildDoc
cmdclass = {'build_flask': BuildDoc}

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()
long_description = (
        read('docs/README.rst')
       )

version = '1.0'
release = version
name = 'towelski'
copyright = 'copyleft'

setup(
    name = name,
    version = version,
    release = release,
    description = "je rêve d'une banque",
    long_description = long_description,
    author = 'Julien Vaucher',
    author_email = 'vtt.leyack@gmail.com',
    license = 'Apache Software License',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools','graphviz'],
    zip_safe = False,
    cmdclass = cmdclass,
    command_options = {
        'build_flask': {
            'project': ('setup.py', name),
            'copyright' : ('setup.py', copyright),
            'version': ('setup.py', version),
            'release': ('setup.py', release),
            'source_dir': ('setup.py', 'docs')}},
)

