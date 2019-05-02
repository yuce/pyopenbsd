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
      download_url="https://github.com/yuce/pyopenbsd",
      author="Yuce Tekol",
      author_email="yucetekol@gmail.com",
      description="OpenBSD Library",
      long_description=long_description,
      long_description_content_type="text/markdown",
      license="BSD",
      packages=["openbsd"],
      keywords=["OpenBSD"],
      setup_requires=["cffi>=1.12.3"],
      cffi_modules=["openbsd/openbsd_builder.py:ffibuilder"],
      install_requires=["cffi>=1.12.3"],
      tests_require=["pytest", "pytest-cov"],
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Operating System :: POSIX :: BSD :: OpenBSD",
        "License :: OSI Approved :: BSD License",
    ],

)
