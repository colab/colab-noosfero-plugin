#!/usr/bin/env python
"""
colab-noosfero plugin
===================

A Noosfero plugin for Colab.
"""
from setuptools import setup, find_packages

install_requires = ['colab']

tests_require = ['mock']


setup(
    name="colab-noosfero",
    version='0.2.4',
    author='Sergio Oliveira',
    author_email='sergio@tracy.com.br',
    url='https://github.com/colab/colab-noosfero-plugin',
    description='A Noosfero plugin for Colab',
    long_description=__doc__,
    license='GPLv3',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    test_suite="tests.runtests.run",
    tests_require=tests_require,
    extras_require={'test': tests_require},
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
