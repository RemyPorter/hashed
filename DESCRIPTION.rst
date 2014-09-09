# Hashed
It accepts any string of hexadecimal characters and returns a string of words that uniquely maps to that hash.

```
>>> from hashed.words import dehash, enhash
>>> dehash("21046fd2f17ac0f30c88190393568045256866f2")
'cassareep irascibly upbrought scorched atheized bourtrees oloroso manful chobdar hornbook'
>>> enhash('disbowel obi magnetises famous oblivious divulgence thickened welders foiningly votresses')
'3bc491b57f3a4d1a91da3daae16dfa0052aff75f'
```

As a note, that module has broader uses, like making more readable representations of IPv6 addresses. It's currently weak on error handling, and will explode if you throw input at it that doesn't fit the wordlist.

### The Wordlist
The Wordlist is a space-padded file, with a word every 15 characters (or every 30 bytes). It was designed this way for fast access. There is also a JSON encoded index to support the reverse lookup.