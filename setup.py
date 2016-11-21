#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" package setup screen """
import os
import sys
import codecs
from setuptools import setup
import rrl

NAME = 'rrl'
DESC = 'Meta-language for artifacts generation'
VERSION = rrl.__version__
AUTHOR = 'João Pinto'
AUTHOR_EMAIL = 'lamego DOT pinto AT gmail DOT com'
LICENSE = 'MIT'
URL = 'https://github.com/joaompinto/rrl'
DOWNLOAD_URL = 'https://github.com/joaompinto/textX/rrl/v%s.tar.gz' \
    % VERSION
README = codecs.open(os.path.join(os.path.dirname(__file__), 'README.adoc'),
                     'r', encoding='utf-8').read()


if sys.argv[-1].startswith('publish'):
    if os.system("pip list | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip list | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    if sys.argv[-1] == 'publishtest':
        os.system("twine upload -r test dist/*")
    else:
        os.system("twine upload dist/*")
        print("You probably want to also tag the version now:")
        print("  git tag -a {0} -m 'version {0}'".format(VERSION))
        print("  git push --tags")
    sys.exit()

setup(
    name=NAME,
    version=VERSION,
    description=DESC,
    long_description=README,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    license=LICENSE,
    url=URL,
    download_url=DOWNLOAD_URL,
    packages=["rrl", "rrl.commands"],
    install_requires=["textx"],
    keywords="parser meta-language",
    entry_points={
        'console_scripts': [
            'rrl=rrl.commands.console:rrl'
        ]
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ]

)
