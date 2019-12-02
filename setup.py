#!/usr/bin/env python3
import os
from setuptools import find_packages

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

PACKAGE_PATH = os.path.abspath(os.path.join(__file__, os.pardir))

setup(name='tfkt',
      version='0.1',
      description='A generic tf.keras design pattern.',
      url='https://github.com/rgmyr/tfkt',
      author='Ross Meyer',
      author_email='ross.meyer@utexas.edu',
      packages=find_packages(PACKAGE_PATH),
      install_requires=[
            'numpy >= 1.13.0',
      ],
      zip_safe=False
)
