#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Keyword
from secretpy import alphabets

alphabet = alphabets.GERMAN
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = "queenly"

cipher = Keyword();
print(plaintext)

enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)

#######################################################

print("----------------------------------")

plaintext  = u"thisisasecretmessage"
key = "keyword"

# use default english alphabet
print(plaintext)
enc = cipher.encrypt(plaintext, key)
print(enc)
dec = cipher.decrypt(enc, key)
print(dec)
