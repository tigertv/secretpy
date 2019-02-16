#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Zigzag

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = 3

chipher = Zigzag();
'''
print(plaintext)

enc = chipher.encrypt(key, plaintext, alphabet)
print(enc)
dec = chipher.decrypt(key, enc, alphabet)
print(dec)

#######################################################

print("----------------------------------")

plaintext  = u"wearediscoveredfleeatonce"

print(plaintext)
enc = chipher.encrypt(key, plaintext)
print(enc)
dec = chipher.decrypt(key, enc)
print(dec)

#######################################################
'''

print("----------------------------------")

plaintext  = u"defendtheeastwallofthecastle"
key = 4

print(plaintext)
enc = chipher.encrypt(key, plaintext)
print(enc)
dec = chipher.decrypt(key, enc)
print(dec)
