#!/usr/bin/env python

from distutils.core import setup
import fauxcker

setup(
    name='Fauxcker',
    version=fauxcker.__version__,
    description='Python recreation of the Docker container engine',
    author='Michael Peppers',
    author_email='mcgdevfunk824@protonmail.com',
    url="https://www.python.org/sigs/distutils-sig/',
    packages=['distutils', 'distutils.command'],
    scripts=['scripts/fauxcker'])
