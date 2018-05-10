#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 
                'requirements-parser'
                ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Christopher Tunnell",
    author_email='christopher.douglas.tunnell+ripa@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="This tool helps you handle requirements.txt installations (e.g. in CI) where uses Anaconda for some packages but also wants pip packages.",
    entry_points={
        'console_scripts': [
            'ripa=ripa.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ripa',
    name='ripa',
    packages=find_packages(include=['ripa']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/tunnell/ripa',
    version='0.2.0',
    zip_safe=False,
)
