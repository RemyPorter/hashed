from setuptools import setup

setup(
	name="hashedwords",
	version="1.0.1",
	description="A module that converts hexadecimal digits into strings of words, and back",
	long_description = """
It accepts any string of hexadecimal characters and returns a string of words that uniquely maps to that hash.

::
	>>> from hashed import dehash, enhash
	>>> dehash("21046fd2f17ac0f30c88190393568045256866f2")
	'cassareep irascibly upbrought scorched atheized bourtrees oloroso manful chobdar hornbook'
	>>> enhash('disbowel obi magnetises famous oblivious divulgence thickened welders foiningly votresses')
	'3bc491b57f3a4d1a91da3daae16dfa0052aff75f'

As a note, that module has broader uses, like making more readable representations of IPv6 addresses. It's currently weak on error handling, and will explode if you throw input at it that doesn't fit the wordlist.

The Wordlist is a space-padded file, with a word every 15 characters (or every 30 bytes). It was designed this way for fast access. There is also a JSON encoded index to support the reverse lookup.
	""",
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
	packages=['hashed'],
	package_dir={'hashed':'hashed'},
	package_data={
		'hashed': ['data/*']
	}
)
