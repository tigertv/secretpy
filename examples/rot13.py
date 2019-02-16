#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot13 

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = u""

cipher = Rot13();
print(plaintext)

enc = cipher.encrypt(key, plaintext, alphabet)
print(enc)
dec = cipher.decrypt(key, enc, alphabet)
print(dec)

#######################################################

print("----------------------------------")

plaintext  = u"thisisasecretmessage"

print(plaintext)

# use default english alphabet 5x5
enc = cipher.encrypt(key, plaintext)
print(enc)
dec = cipher.decrypt(key, enc)
print(dec)
