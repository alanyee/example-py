example-py
========================
Example Template for Python Module Library

|Unit Tests|

.. |Unit Tests| image:: https://github.com/alanyee/example-py/actions/workflows/test.yml/badge.svg
    :target: https://github.com/alanyee/example-py/actions/workflows/test.yml
    :alt: Unit Tests

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
