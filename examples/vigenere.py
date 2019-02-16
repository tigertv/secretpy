#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Vigenere

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = u"kss"

chipher = Vigenere();
print(plaintext)

enc = chipher.encrypt(key, plaintext, alphabet)
print(enc)
dec = chipher.decrypt(key, enc, alphabet)
print(dec)

#######################################################

print("----------------------------------")

plaintext  = u"attackatdawn"
key      = u"lemon"

print(plaintext)
enc = chipher.encrypt(key, plaintext)
print(enc)
dec = chipher.decrypt(key, enc)
print(dec)
