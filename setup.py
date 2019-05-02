# Author: yuce
# Created on: 2019-05-03, at: 01:50 +0300

import sys
import os
import io
import os.path
from setuptools import setup

with io.open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(name="openbsd",
      version="0.1.0",
      url="",
      download_url="",
      author="yuce",
      author_email="",
      description="",
      long_description=long_description,
      long_description_content_type="text/markdown",
      license="",
      packages=["openbsd"],
      keywords=["OpenBSD"],
      setup_requires=["cffi>=1.12.3"],
      cffi_modules=["openbsd/openbsd_builder.py:ffibuilder"],
      install_requires=["cffi>=1.12.3"],
      tests_require=["pytest", "pytest-cov"],
      classifiers=[],
)
