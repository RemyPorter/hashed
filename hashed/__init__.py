"""
A module to create a friendly representation of an underlying hash object. Uses wordlist as its source data.

wordlist is a UTF-16 encoded file with one string every bytes.

>>> testhash = '21046fd2f17ac0f30c88190393568045256866f2'
>>> dehash(testhash)
'cassata irately upbuild scorchers atheizing bouse olpe manfulness choc hornbooks'
>>> enhash('cassata irately upbuild scorchers atheizing bouse olpe manfulness choc hornbooks')
'21046fd2f17ac0f30c88190393568045256866f2'
>>> testhash == enhash('cassata irately upbuild scorchers atheizing bouse olpe manfulness choc hornbooks')
True
"""
import inspect, os.path, gzip, json
from mmap import mmap
from collections import namedtuple

__file = None
__mapped = None
__index = None

def __init__():
	global __file, __mapped, __index
	__base = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
	__file = open(os.path.join(__base, "data","wordlist"), "r+b")
	__mapped = mmap(__file.fileno(),0)
	__index = None
	with gzip.open(os.path.join(__base,"data","index"), "rb") as f:
		data = f.read()
		__index = json.loads(data.decode("UTF8"))

__init__()

def shorten(wordstring):
	"""Given a list of words, grab the first and last word.
	>>> shorten('scatology solen courtier retrofit unmasking scantling carjacks arrestors nunship puffball')
	'scatology puffball'
	"""
	array = wordstring.split(" ")
	return array[0] + " " + array[-1]

def dehash(hash, address_size=4,line_size=15,character_size=2):
	"""Given a string containing hexadecimal digits, returns a FriendlyHash tuple containing the original string and a "friendly" version
	from mappedhash. Depends on the contents of wordlist. Address size is the number of hex digits used per word,
	and should be related to the underlying word-file. Line size is how many characters make up a word block, and character size
	is the number of bytes per character.

	>>> dehash("3bc491b57f3a4d1a91da3daae16dfa0052aff75f")
	'disbud obiing magnetite famousness oblong divulges thickening welding foins vouched'
	>>> dehash("bff2cdc22f22b79fee98bfa3205a0b12912fabd0")
	'scats solenettes courtiers retrofits unmasks scantlings carking arrests nuraghi puffer'
    >>> dehash("00")
    'aah'
	"""
	global __file, __mapped
	words = []
	f = __file
	mapped = __mapped
	for i in range(0, len(hash), address_size):
		hx = "00"
		try:
			hx = hash[i:i+address_size]
		except IndexError as err:
			hx = hash[-address_size:0]

		line = int(hx, 16)
		word = get_at_address(line, line_size, character_size)
		words += [word]
	return " ".join(words)

def get_at_address(line, line_size, character_size):
	address = line_size * character_size * line #-line_size*character_size
	word = __mapped[address:address+line_size*character_size]
	return word.decode("UTF16").strip()	

def enhash(words, address_size=4):
	"""
	Given a word string, containing only words in wordlist, return the hash that it comes from. This assumes that the supplied 
	wordlist only contains "valid" words, off the wordlist list. It may enter an infinite loop otherwise. (I will fix that, probably)
	>>> enhash('disbowel obi magnetises famous oblivious divulgence thickened welders foiningly votresses')
	'3bc391b47f394d1991d93da9e16cf9ff52aef75e'
	>>> enhash('scatology solen courtier retrofit unmasking scantling carjacks arrestors nunship puffball')
	'bff1cdc12f21b79eee97bfa220590b11912eabcf'
	"""
	l = words.split(" ")
	test = ""
	hsh = ""
	for word in l:
		(bottom,top) = __index[word]

		hsh += hex(bottom // 30)[2:].rjust(address_size, "0")
	return hsh

def get_index():
	return __index


FriendlyHash = namedtuple("FriendlyHash", "hash friendly")

if __name__ == "__main__":
    import doctest
    doctest.testmod()


