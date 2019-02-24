SecretPy
===========

[![](https://badge.fury.io/py/secretpy.svg)](https://pypi.org/project/secretpy)
[![](https://img.shields.io/pypi/pyversions/secretpy.svg)](https://pypi.org/project/secretpy)

***Download:***

https://pypi.org/project/secretpy

***Source code & Development:***

https://github.com/tigertv/secretpy

Description
-----------

SecretPy is a cryptographic library. It uses the following classical cipher algorithms:

- ADFGX
- ADFGVX
- Affine
- Atbash
- Autokey
- Beaufort 
- Bifid
- Caesar
- Keyword
- Monoalphabet
- Polybius
- Rot5
- Rot13
- Trifid
- Vigenere
- Zigzag


Installation
------------

To install this library, you can use pip:

```bash
pip install secretpy
```

Alternatively, you can install the package using the repo's cloning and the make:

```bash
git clone https://github.com/tigertv/secretpy
cd secretpy
make install
```

Usage
-----

```python
#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Caesar

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = Caesar()

print(plaintext)
enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)

print('=====================================')

print(plaintext)
# use default english alphabet
enc = cipher.encrypt(plaintext, key)
print(enc)
dec = cipher.decrypt(enc, key)
print(dec)

'''
Output:

thequickbrownfoxjumpsoverthelazydog
wkhtxlfneurzqirämxpsvryhuwkhodüögrj
thequickbrownfoxjumpsoverthelazydog
=====================================
thequickbrownfoxjumpsoverthelazydog
wkhtxlfneurzqiramxpsvryhuwkhodcbgrj
thequickbrownfoxjumpsoverthelazydog
'''
```

You can use CryptMachine and decorators for that:

```python
#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Atbash 
from secretpy import Caesar

from secretpy import CryptMachine 
from secretpy.cmdecorators import *

def encdec(machine, plaintext):
	print(plaintext)
	enc = machine.encrypt(plaintext)
	print(enc)
	dec = machine.decrypt(enc)
	print(dec)
	print("-----------------------------------")

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = Caesar()

cm = CryptMachine(cipher, key)
encdec(cm, plaintext)

cm.setAlphabet(alphabet)
encdec(cm, plaintext)

cm = SaveSpaces(cm)
cm.setKey(9)
plaintext  = u"the quick brown fox jumps over the lazy dog"
encdec(cm, plaintext)

cm = NoSpaces(UpperCase(cm))
cm.setCipher(Atbash())
plaintext  = u"Achtung Minen"
encdec(cm, plaintext)

'''
Output:

thequickbrownfoxjumpsoverthelazydog
wkhtxlfneurzqiramxpsvryhuwkhodcbgrj
thequickbrownfoxjumpsoverthelazydog
-----------------------------------
thequickbrownfoxjumpsoverthelazydog
wkhtxlfneurzqirämxpsvryhuwkhodüögrj
thequickbrownfoxjumpsoverthelazydog
-----------------------------------
the quick brown fox jumps over the lazy dog
üqn zßrlt käxbw oxc sßvyö xanä üqn ujed mxp
the quick brown fox jumps over the lazy dog
-----------------------------------
Achtung Minen
ßÖWKJQXRVQZQ
ACHTUNGMINEN
-----------------------------------
'''
```

Maintainers
-----------

- [@tigertv](https://github.com/tigertv) (Max Vetrov)


