#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Caesar

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
chipher = Caesar();

enc = chipher.encrypt(key, plaintext, alphabet)
print(enc)
dec = chipher.decrypt(key, enc, alphabet)
print(dec)

# use default english alphabet
enc = chipher.encrypt(key, plaintext)
print(enc)
dec = chipher.decrypt(key, enc)
print(dec)
