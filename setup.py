# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

from setuptools import setup, find_packages

# Try to convert markdown README to rst format for PyPI.
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description_content_type='text/x-rst'
except(IOError, ImportError):
    long_description = open('README.md').read()
    long_description_content_type='text/markdown'

setup(
    name='cohesity_management_sdk',
    version='1.9.2',
    description='This SDK provides operations for interfacing with the Cohesity Cluster.',
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    author='Cohesity Inc.',
    author_email='cohesity-api-sdks@cohesity.com',
    url='https://github.com/cohesity/management-sdk-python',
    packages=find_packages(),
    install_requires=[
        'requests>=2.9.1, <3.0',
        'cachecontrol>=0.11.7, <1.0',
        'python-dateutil>=2.5.3, <3.0'
    ]
)
