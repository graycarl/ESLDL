# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='ESLDL',
    version='0.1',
    py_modules=['esldl'],
    install_requires=[
        'Click',
        'BeautifulSoup4',
        'Requests'
    ],
    entry_points="""
        [console_scripts]
        esldl=esldl:cli
    """
)
