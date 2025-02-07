#!/usr/bin/env python

# Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011, 2012  Andrey Golovizin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import os

from setuptools import find_packages, setup

from pybtex.__version__ import version

progname = "pybtex"

ROOT = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(ROOT, "README")).read()

install_requires = ["PyYAML>=3.01"]

setup(
    name=progname,
    version=version,
    description="A BibTeX-compatible bibliography processor in Python",
    long_description=README,
    author="Andrey Golovizin",
    author_email="ag@sologoc.com",
    url="http://pybtex.sourceforge.net/",
    license="MIT",
    platforms=["platform-independent"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Markup :: LaTeX",
        "Topic :: Text Processing :: Markup :: XML",
        "Topic :: Utilities",
    ],
    install_requires=install_requires,
    packages=find_packages(exclude=["docs"]),
    scripts=[
        os.path.join("scripts", progname),
        os.path.join("scripts", progname + "-convert"),
        os.path.join("scripts", progname + "-format"),
    ],
    include_package_data=True,
    entry_points={
        "pybtex.database.input": [
            "bibtex = pybtex.database.input.bibtex:Parser",
            "bibtexml = pybtex.database.input.bibtexml:Parser",
            "yaml = pybtex.database.input.bibyaml:Parser",
        ],
        "pybtex.database.input.aliases": [
            "bibyaml = pybtex.database.input.bibyaml:Parser",
        ],
        "pybtex.database.input.suffixes": [
            ".bib = pybtex.database.input.bibtex:Parser",
            ".xml = pybtex.database.input.bibtexml:Parser",
            ".bibtexml = pybtex.database.input.bibtexml:Parser",
            ".bibyaml = pybtex.database.input.bibyaml:Parser",
            ".yaml = pybtex.database.input.bibyaml:Parser",
        ],
        "pybtex.database.output": [
            "bibtex = pybtex.database.output.bibtex:Writer",
            "bibtexml = pybtex.database.output.bibtexml:Writer",
            "yaml = pybtex.database.output.bibyaml:Writer",
        ],
        "pybtex.database.output.aliases": [
            "bibyaml = pybtex.database.output.bibyaml:Writer",
        ],
        "pybtex.database.output.suffixes": [
            ".bib = pybtex.database.output.bibtex:Writer",
            ".xml = pybtex.database.output.bibtexml:Writer",
            ".bibtexml = pybtex.database.output.bibtexml:Writer",
            ".bibyaml = pybtex.database.output.bibyaml:Writer",
            ".yaml = pybtex.database.output.bibyaml:Writer",
        ],
        "pybtex.backends": [
            "latex = pybtex.backends.latex:Backend",
            "html = pybtex.backends.html:Backend",
            "plaintext = pybtex.backends.plaintext:Backend",
        ],
        "pybtex.backends.aliases": [
            "text = pybtex.backends.plaintext:Backend",
        ],
        "pybtex.backends.suffixes": [
            ".bbl = pybtex.backends.latex:Backend",
            ".tex = pybtex.backends.latex:Backend",
            ".latex = pybtex.backends.latex:Backend",
            ".html = pybtex.backends.html:Backend",
            ".txt = pybtex.backends.plaintext:Backend",
        ],
        "pybtex.style.labels": [
            "number = pybtex.style.labels.number:LabelStyle",
            "alpha = pybtex.style.labels.alpha:LabelStyle",
        ],
        "pybtex.style.names": [
            "plain = pybtex.style.names.plain:NameStyle",
            "lastfirst = pybtex.style.names.lastfirst:NameStyle",
            "last_first = pybtex.style.names.lastfirst:NameStyle",
        ],
        "pybtex.style.sorting": [
            "none = pybtex.style.sorting.none:SortingStyle",
            "author_year_title = pybtex.style.sorting.author_year_title:SortingStyle",
        ],
        "pybtex.style.formatting": [
            "plain = pybtex.style.formatting.plain:Style",
            "unsrt = pybtex.style.formatting.unsrt:Style",
            "alpha = pybtex.style.formatting.alpha:Style",
            "unsrtalpha = pybtex.style.formatting.unsrtalpha:Style",
        ],
    },
    zip_safe=True,
)
