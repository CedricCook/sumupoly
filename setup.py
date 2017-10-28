#!/usr/bin/python

from distutils.core import setup

setup(
    name='SumuPoly',
    version='0.0.1',
    description='A small Django app to interact with SumUp for AGEPoly - EPFL',
    long_description='SumuPoly is a Django app that can be used to obtain detailed reports about transactions generated using the SumUp payment system and its API. It is so far only useful for AGEPoly, EPFLs general students association',
    author='Cedric Cook',
    author_email='trash@agepoly.ch',
    url='https://github.com/CedricCook/sumupoly',
    packages=[
        'sumupoly',
    ],
    include_package_data=True,
    install_requires=[
        'django<1.7',
        'django-bootstrap3',
    ]
)
