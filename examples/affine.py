#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Affine

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = [7,8]

chipher = Affine();
print(plaintext)

enc = chipher.encrypt(key, plaintext, alphabet)
print(enc)
dec = chipher.decrypt(key, enc, alphabet)
print(dec)

#######################################################

print("----------------------------------")

key = [3,4]
plaintext  = u"attackatdawn"

# use default english alphabet
print(plaintext)
enc = chipher.encrypt(key, plaintext)
print(enc)
dec = chipher.decrypt(key, enc)
print(dec)
