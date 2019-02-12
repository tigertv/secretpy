# SecretPy

Classical cipher algorithms


Installation:
```
pip install secretpy
```

Sample usage:

```python
#!/usr/bin/python
from secretpy import Caesar

alphabet = u"abcdefghijklmnopqrstuvwxyz"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
enc = Caesar().encrypt(alphabet, key, plaintext)
print(enc)
dec = Caesar().decrypt(alphabet, key, enc)
print(dec)

```

It uses Python 2.7
