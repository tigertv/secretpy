#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Vigenere
from secretpy import alphabets

alphabet = alphabets.GERMAN
plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = u"kss"

cipher = Vigenere()
print(plaintext)

enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)

#######################################################

print("----------------------------------")

plaintext = u"attackatdawn"
key = u"lemon"

print(plaintext)
enc = cipher.encrypt(plaintext, key)
print(enc)
dec = cipher.decrypt(enc, key)
print(dec)

'''
thequickbrownfoxjumpsoverthelazydog
ßzwäiämütöckxxcdöiwdgyjwöhzoßsfmvyy
thequickbrownfoxjumpsoverthelazydog
----------------------------------
attackatdawn
lxfopvefrnhr
attackatdawn
'''
