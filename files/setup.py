#!/usr/bin/env python

from setuptools import setup

version = open("files/version.txt").read().strip()
long_description = open("README.md").read().strip()

setup(
    name='Phishe',
    version=version,
    description='A python phishing script for login phishing, image phishing video phishing an many more!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='KasRoudra',
    author_email='youssefallali210@gmail.com',
    license="MIT",
    url='https://github.com/youssefallali/Phishe/',
    scripts=['phishe'],
    install_requires=["requests", "bs4", "rich"]
)
