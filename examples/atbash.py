#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Atbash

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = ""

chipher = Atbash();
print(plaintext)

enc = chipher.encrypt(key, plaintext, alphabet)
print(enc)
dec = chipher.decrypt(key, enc, alphabet)
print(dec)

#######################################################

print("----------------------------------")

plaintext  = u"attackatdawn"

# use default english alphabet
print(plaintext)
enc = chipher.encrypt(key, plaintext)
print(enc)
dec = chipher.decrypt(key, enc)
print(dec)
