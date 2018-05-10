============================================
Resolve Installations using Pip and Anaconda
============================================


.. image:: https://img.shields.io/pypi/v/ripa.svg
        :target: https://pypi.python.org/pypi/ripa

.. image:: https://img.shields.io/travis/tunnell/ripa.svg
        :target: https://travis-ci.org/tunnell/ripa


This tool helps you handle requirements.txt installations (e.g. in CI) where uses Anaconda for some packages but also wants pip packages.


* Free software: GNU General Public License v3
* Documentation: https://ripa.readthedocs.io.

Install
-------

Installation can be done via PyPI::

  pip install ripa

Or through this repository by::

  python setup.py install

Usage
-----

Point `ripa` at your requirements file and then let 'er rip::

  ripa --file requirements.txt


