from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "DESCRIPTION.rst"), encoding="UTF8") as f:
	long_desc = f.read()

setup(
	name="Hashed Words",
	version="1.0.0",
	description="A module that converts hexadecimal digits into strings of words, and back",
	long_description = long_desc,
	url="https://github.com/RemyPorter/hashed",
	author="Remy Porter",
	author_email="remyporter@jetpackshark.com",
	license="MIT",
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
	],
	keywords="development hashes words",
	package_data={
		'wordlist':['wordlist'],
		'index':['index']
	}
)
