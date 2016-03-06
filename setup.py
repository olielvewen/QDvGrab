#!/usr/bin/env python
#-*- coding: uft-8 -*-

import src
from distutils.core import setup

data_files = [('xdg/applications/', ['data/qdvgrab.desktop']),
               ('xdg/icons', ['data/qdvgrab.png'])]

setup(
    name='qdvgrab',
    packages=['qdvgrab'],
    script_args=['qdvgrab/launch'],
    data_files='data_files',
    version='0.10',
    description='GUI for Dvgrab',
    author='Olivier Girard',
    author_email='olivier@openshot.org',
    url='https://github.com/olielvewen/QDvGrab/',
    download_url='https://github.com/olielvewen/QDvGrab/',
    license='GNU GPL3',
    platforms='Linux',
    keywords=['transfert', 'grab', 'video', 'film'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX :: Linux',
        'Development Status :: 3 - Alpha',
        'Environment :: x11 Applications :: Qt',
        'Natural Language :: English',
        'Natural Language :: French',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Video :: Capture',
    ],
    long_description= """
QdvGrab
-------

Simple Gui for dvgrab, QDvGrab is simple to use too. This is the main idea for this project i.e easy to install, easy to
 use. None command lines needs. With QDvGrab you grab your films from a DV or HDV Camcorder in an easy way.

Features:
 - Nice interface
 - Simple utilisation
 - Modern programm
 - Complete Preferences
 - Essential features of dvgrab
 - No command lines for dvgrab

Requires : python3, PyQt5, dvgrab, Qt5
"""
)