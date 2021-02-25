example-py
========================
Example Template for Python Module Library

|Unit Tests|

.. |Unit Tests| image:: https://github.com/alanyee/example-py/actions/workflows/test.yml/badge.svg
    :target: https://github.com/alanyee/example-py/actions/workflows/test.yml
    :alt: Unit Tests

Want to know how to create the badge above? Learn more about `GitHub Actions`_ 

.. _GitHub Actions: https://docs.github.com/en/actions/guides/building-and-testing-python

Getting Started
---------------
Assuming that you have Python 3 installed, set up your environment and install the required dependencies like this:

.. code-block:: sh

    $ git clone https://github.com/alanyee/example-py
    $ cd example-py
    $ python3 -m venv venv
    ...
    $ . venv/bin/activate
    $ python -m pip install -e .

Running Tests
~~~~~~~~~~~~~
You can run tests in all supported Python versions using ``pytest``.

.. code-block:: sh

    $ python -m pip install -e '.[testing]'
    $ python -m pytest -s -v

Generating the Docs
~~~~~~~~~~~~~
You can generate the docs yourself. If the docs have not been generated already:

.. code-block:: sh

    $ python -m pip install -r requirements-docs.txt
    $ mkdir docs && cd docs
    $ sphinx-quickstart
    ...
    # After the files are generated,
    # Uncomment ``import os``, ``import sys``, and ``sys.path.insert(0, os.path.abspath('.'))``
    # Change `sys.path.insert(0, os.path.abspath('.'))`` to `sys.path.insert(0, os.path.abspath('..'))``
    # Add ``'sphinx.ext.autodoc'`` to the ``extensions`` list
    # Add ``modules`` to index.rst
    $ sphinx-apidoc -o . .. ../setup.py 
    $ make html

If you are making changes to documentation, run:

.. code-block:: sh

    $ sphinx-apidoc -o . .. ../setup.py -f
    $ make html
