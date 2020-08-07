# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in app_test/__init__.py
from app_test import __version__ as version

setup(
	name='app_test',
	version=version,
	description='test-app by stericano',
	author='stericano',
	author_email='tershiro@windowslive.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
