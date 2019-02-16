# SecretPy

Classical cipher algorithms

- ADFGX
- Affine
- Atbash
- Autokey
- Beaufort 
- Caesar
- Keyword
- Monosub
- Polybius
- Rot13
- Vigenere
- Zigzag

Installation:
```bash
pip install secretpy
```

Sample code:

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

Sample with CryptMachine:

```python
#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import CryptMachine 
from secretpy import Caesar
from secretpy import Atbash 

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = Caesar()

print("-----------------------------------")

machine = CryptMachine(cipher, key);
enc = machine.encrypt(plaintext)
print(enc)
dec = machine.decrypt(enc)
print(dec)

print("-----------------------------------")

machine.setAlphabet(alphabet)
enc = machine.encrypt(plaintext)
print(enc)
dec = machine.decrypt(enc)
print(dec)

print("-----------------------------------")

machine.setKey(9)
enc = machine.encrypt(plaintext)
print(enc)
dec = machine.decrypt(enc)
print(dec)

print("-----------------------------------")

machine.setCipher(Atbash())
enc = machine.encrypt(plaintext)
print(enc)
dec = machine.decrypt(enc)
print(dec)
```

It uses Python 2.7
