SecretPy
===========

[![Go to PyPi](https://badge.fury.io/py/secretpy.svg)](https://pypi.org/project/secretpy)
[![Go to PyPi](https://img.shields.io/pypi/pyversions/secretpy.svg)](https://pypi.org/project/secretpy)
[![Read the Docs](https://img.shields.io/readthedocs/secretpy.svg)](https://secretpy.readthedocs.io/en/latest)

***Download:***

https://pypi.org/project/secretpy

***Documentation:***

https://secretpy.readthedocs.io

***Source code & Development:***

https://github.com/tigertv/secretpy

Description
-----------

SecretPy is a cryptographic Python package. It uses the following classical cipher algorithms:

- ADFGX, ADFGVX
- Affine
- Atbash
- Autokey
- Beaufort 
- Bifid
- Caesar
- Keyword
- Monoalphabet
- Polybius
- Rot13, Rot5, Rot18, Rot47
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
from secretpy import alphabet

alphabet = alphabet.GERMAN
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

In the previous example plaintext contains letters only in the alphabet.
To change the behaviour you can use CryptMachine and decorators(UpperCase, NoSpace, SaveCase and etc.):

```python
#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Atbash 
from secretpy import Caesar

from secretpy import CryptMachine 
from secretpy.cmdecorators import *
from secretpy import alphabet

def encdec(machine, plaintext):
	print(plaintext)
	enc = machine.encrypt(plaintext)
	print(enc)
	dec = machine.decrypt(enc)
	print(dec)
	print("-----------------------------------")

plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = Caesar()

cm = CryptMachine(cipher, key)
encdec(cm, plaintext)

cm.setAlphabet(alphabet.GERMAN)
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

Combining several ciphers to get more complex cipher, you can use CompositeMachine:

```python
#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot13
from secretpy import Caesar
from secretpy import CryptMachine
from secretpy import CompositeMachine
from secretpy.cmdecorators import *

def encdec(machine, plaintext):
	print("=======================================")
	print(plaintext)
	enc = machine.encrypt(plaintext)
	print(enc)
	dec = machine.decrypt(enc)
	print(dec)

key = 5
plaintext = u"Dog jumps four times and cat six times"
print(plaintext)

cm1 = SaveSpaces(SaveCase(CryptMachine(Caesar(), key)))
enc = cm1.encrypt(plaintext)
print(enc)

cm2 = SaveSpaces(SaveCase(CryptMachine(Rot13())))
enc = cm2.encrypt(enc)
print(enc)

print("=======================================")

cm = CompositeMachine(cm1)
cm.addMachine(cm2)
enc = cm.encrypt(plaintext)
print(enc)

encdec(cm, plaintext)

cm.addMachine(cm1, cm2)
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

