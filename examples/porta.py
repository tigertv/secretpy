#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Porta
from secretpy import alphabets

alphabet = alphabets.GERMAN
plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = u"dogs"

cipher = Porta()
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
dßwheputrkrnßöroznpgcvdübmzüöwhatvy
thequickbrownfoxjumpsoverthelazydog
----------------------------------
attackatdawn
seauvppaxtel
attackatdawn
'''
