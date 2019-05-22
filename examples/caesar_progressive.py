#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import CaesarProgressive
from secretpy import alphabets

alphabet = alphabets.ENGLISH
plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = CaesarProgressive()

print(plaintext)
enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)

print('=====================================')

print(plaintext)
# use default english alphabet
enc = cipher.encrypt(plaintext, key)
print(enc)
dec = cipher.decrypt(enc, key)
print(dec)

'''
thequickbrownfoxjumpsoverthelazydog
wljwbqlumdbkcvfpcohlpmuesvkiqgggmyr
thequickbrownfoxjumpsoverthelazydog
=====================================
thequickbrownfoxjumpsoverthelazydog
wljwbqlumdbkcvfpcohlpmuesvkiqgggmyr
thequickbrownfoxjumpsoverthelazydog
'''
