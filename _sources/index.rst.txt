.. notutils documentation master file, created by
   sphinx-quickstart on Tue Jul 15 07:31:20 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

notutils documentation
======================

Jupyter Notebook Utilities for Python

notutils is a collection of convenience functions designed to enhance the Jupyter Notebook experience for Python users. It provides convenient tools for displaying URLs, embedding iframes, visualizing Google Books, toggling code visibility, creating interactive prediction widgets, and more.

Quick Start
-----------

.. code-block:: python

   from notutils import display_url, iframe_url, display_iframe_url

   display_url("https://github.com/lawrennd/notutils")
   iframe_html = iframe_url("https://www.example.com", width=800, height=400)
   display_iframe_url("https://www.example.com", width=800, height=400)

Installation
------------

.. code-block:: bash

   pip install notutils

   # or with Poetry
   poetry add notutils

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api

