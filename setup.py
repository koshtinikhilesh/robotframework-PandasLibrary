#!/usr/bin/env python

from os.path import join, dirname
from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()

DESCRIPTION = """
Pandas Module support for Robot Framework.
"""[1:-1]

setup(name         = 'robotframework-pandaslibrary',
      version      = '0.0.1',
      description  = 'Pandas Module support library for Robot Framework',
      long_description = DESCRIPTION,
      author       = 'Koshti Nikhilesh',
      author_email = 'koshtinikhilesh1993@gmail.com',
      url          = 'https://github.com/koshtinikhilesh/robotframework-PandasLibrary',
      license      = 'Apache License 2.0',
      keywords     = 'robotframework testing pandas csv',
      platforms    = 'any',
      classifiers  = [
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Testing"
      ],
      install_requires = [
          'robotframework >= 2.6.0',
      ],
      packages    = ['PandasLibrary'],
      )
