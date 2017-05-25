#! /usr/bin/env python

try:
    import setuptools
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()

from setuptools import setup, find_packages

NAME = "Oasys-Widget-Core"
VERSION = "0.0.4"
DESCRIPTION = "Core orange widget utilities"
LONG_DESCRIPTION = open("README.txt", "rt").read()

URL = "http://orange.biolab.si/"
AUTHOR = "Bioinformatics Laboratory, FRI UL"
AUTHOR_EMAIL = 'contact@orange.biolab.si'

LICENSE = "GPLv3"
DOWNLOAD_URL = 'https://github.org/lucarebuffi/orange-widget-core'
PACKAGES = find_packages()

PACKAGE_DATA = {
    "orangewidget": ["icons/*.svg", "icons/*png"],
}

SETUP_REQUIRES = (
    "setuptools"
)

INSTALL_REQUIRES = (
    "setuptools",
    "oasys-canvas-core>=0.0.1",
)

CLASSIFIERS = (
    "Development Status :: 1 - Planning",
    "Environment :: X11 Applications :: Qt",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    "Topic :: Scientific/Engineering :: Visualization",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Intended Audience :: Education",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
)

if __name__ == "__main__":
    setup(name=NAME,
          version=VERSION,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          url=URL,
          author=AUTHOR,
          author_email=AUTHOR_EMAIL,
          license=LICENSE,
          packages=PACKAGES,
          package_data=PACKAGE_DATA,
          setup_requires=SETUP_REQUIRES,
          install_requires=INSTALL_REQUIRES,
         )

