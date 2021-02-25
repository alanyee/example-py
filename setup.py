# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='example',
    version='0.0.1',
    description='Example Python Library template',
    long_description=readme,
    author='Alan Yee',
    author_email='alanyee@users.noreply.github.com',
    url='https://github.com/alanyee/example-py',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    python_requires='>=3.6',
    extra_require={
        'testing': ["pytest"]
    }
)
