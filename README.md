# SecretPy

Classical cipher algorithms


Installation:
```
pip install secretpy
```

Sample usage:

```python
#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Caesar

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = Caesar();

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

It uses Python 2.7
