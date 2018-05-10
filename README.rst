============================================
Resolve Installations using Pip and Anaconda
============================================


.. image:: https://img.shields.io/pypi/v/ripa.svg
        :target: https://pypi.python.org/pypi/ripa

.. image:: https://img.shields.io/travis/tunnell/ripa.svg
        :target: https://travis-ci.org/tunnell/ripa


This tool helps you handle requirements.txt installations (e.g. in CI) which use Anaconda for packages if that package and version are available, otherwise falls back to pip installing packages through PyPI.


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

The intention is to reproduce the `pip install` syntax.

Point `ripa` at your `requirements file 
<https://pip.readthedocs.io/en/1.1/requirements.html>`_ and then let 'er rip::

  ripa -r requirements.txt

It will then check each requirements and install prefarably though Anaconda, otherwise through pip.

You can also install individual packages::

  ripa pip==10.0
  ripa wheel

