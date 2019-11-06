#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from codecs import open
import subprocess


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "1.0"
readme = open('README.rst').read()


setup(
    name='cruds_dj_adminlte2',
    version=version,
    description="""cruds_dj_adminlte2 is simple drop-in django app that creates CRUD for faster prototyping.""",  # noqa
    long_description=readme,
    author='Tralah M. Brian',
    author_email='briantralah@gmail.com',
    url='https://github.com/TralahM/cruds_dj_adminlte2',
    packages=[
        'cruds_adminlte',
        'cruds_adminlte.templatetags',
    ],
    include_package_data=True,
    install_requires=[
        'django>=2.2',
        'django-crispy-forms==1.7.2',
        'djangoajax==2.3.7',
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-cruds-adminlte',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
