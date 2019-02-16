# SecretPy

Classical cipher algorithms

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

def encdec(machine, plaintext):
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

cm.setKey(9)
encdec(cm, plaintext)

cm.setCipher(Atbash())
encdec(cm, plaintext)
```

It uses Python 2.7
