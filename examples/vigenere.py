#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Vigenere

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = u"kss"

cipher = Vigenere();
print(plaintext)

enc = cipher.encrypt(key, plaintext, alphabet)
print(enc)
dec = cipher.decrypt(key, enc, alphabet)
print(dec)

#######################################################

print("----------------------------------")

plaintext  = u"attackatdawn"
key      = u"lemon"

print(plaintext)
enc = cipher.encrypt(key, plaintext)
print(enc)
dec = cipher.decrypt(key, enc)
print(dec)
