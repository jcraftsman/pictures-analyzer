#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

setup(
    name='pictures_analyzer',
    version='0.0.1',
    packages=find_packages(exclude=["*_tests"]),
    license='Proprietary',
    long_description=open('README.md').read(),
    install_requires=[
        'pillow',
        'pytesseract'
    ],
    entry_points={
        'console_scripts': [
            'pictures_analyzer = pictures_analyzer.__main__:main',
        ],
    },
)
