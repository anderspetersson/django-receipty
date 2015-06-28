#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='django-receipty',
    version="0.1",
    author='Anders Petersson',
    author_email='me@anderspetersson.se',
    description='Receipts for django',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
