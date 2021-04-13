from setuptools import find_packages, setup
#from distutils.core import setup
import versioneer
import sys

try:
	with open('requirements.txt') as f:
		requirements = f.read().splitlines()
except:
	print('requirements.txt not found!')

setup(name='LactucaNN',
	version='0.0.01',
	description="Robbie and Nick's free money machine",
	author='R. Hovious, N. Lundgren',
	author_email='nwlundgren@ucdavis.edu',
	url='https://www.lactuc.at',
	packages=find_packages(),
	include_package_data=True,
	install_requires=requirements
	)


