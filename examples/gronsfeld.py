#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Gronsfeld

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = (4, 7, 9)

cipher = Gronsfeld()
print(plaintext)

enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)

#######################################################

print("----------------------------------")

plaintext = u"attackatdawn"
key = (14, 2, 11)

print(plaintext)
enc = cipher.encrypt(plaintext, key)
print(enc)
dec = cipher.decrypt(enc, key)
print(dec)

'''
thequickbrownfoxjumpsoverthelazydog
xonuörgrkvvbrmxöqßqwösünväqisjßbmsn
thequickbrownfoxjumpsoverthelazydog
----------------------------------
attackatdawn
oveoevovooyy
attackatdawn
'''
