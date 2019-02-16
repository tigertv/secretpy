#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot13 

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = u""

cipher = Rot13();
print(plaintext)

enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)

#######################################################

print("----------------------------------")

plaintext  = u"thisisasecretmessage"

print(plaintext)

# use default english alphabet 5x5
enc = cipher.encrypt(plaintext)
print(enc)
dec = cipher.decrypt(enc)
print(dec)
