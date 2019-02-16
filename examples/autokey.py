#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Autokey

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = "queenly"

cipher = Autokey();
print(plaintext)

enc = cipher.encrypt(key, plaintext, alphabet)
print(enc)
dec = cipher.decrypt(key, enc, alphabet)
print(dec)

#######################################################

print("----------------------------------")

plaintext  = u"attackatdawn"

# use default english alphabet
print(plaintext)
enc = cipher.encrypt(key, plaintext)
print(enc)
dec = cipher.decrypt(key, enc)
print(dec)
