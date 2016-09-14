#!/usr/bin/env python3
from distutils.core import setup

setup(
    name='pydgeot_depdot',
    version='0.1',
    packages=['pydgeot.plugins.depdot'],
    requires=['pydgeot'],
    url='https://github.com/broiledmeat/pydgeot_depdot',
    license='Apache License, Version 2.0',
    author='Derrick Staples',
    author_email='broiledmeat@gmail.com',
    description='Build dependency DOT graph output for Pydgeot.'
)
