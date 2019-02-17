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
- Affine
- Atbash
- Autokey
- Beaufort 
- Caesar
- Keyword
- Monoalphabet
- Polybius
- Rot13
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

enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)

# use default english alphabet
enc = cipher.encrypt(plaintext, key)
print(enc)
dec = cipher.decrypt(enc, key)
print(dec)
```


You can use CryptMachine:

```python
#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import CryptMachine 
from secretpy import Caesar
from secretpy import Atbash 

def encdec(machine, plaintext):
	enc = machine.encrypt(plaintext)
	print(enc)
	dec = machine.decrypt(enc)
	print(dec)
	print("-----------------------------------")

plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = 3

cm = CryptMachine(Caesar(), key)
encdec(cm, plaintext)

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
cm.setAlphabet(alphabet)
encdec(cm, plaintext)

cm.setKey(9)
encdec(cm, plaintext)

cm.setCipher(Atbash())
cm.setUpperCase()
encdec(cm, plaintext)
```

Maintainers
-----------

- [@tigertv](https://github.com/tigertv) (Max Vetrov)


