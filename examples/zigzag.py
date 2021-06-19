#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Zigzag


plaintext = u"thequickbrownfoxjumpsoverthelazydog"
plaintext = u"thequick"
key = 3

chipher = Zigzag()
print(plaintext)

enc = chipher.encrypt(plaintext, key)
print(enc)
dec = chipher.decrypt(enc, key)
print(dec)

#######################################################

print("----------------------------------")

plaintext = u"wearediscoveredfleeatonce"

print(plaintext)
enc = chipher.encrypt(plaintext, key)
print(enc)
dec = chipher.decrypt(enc, key)
print(dec)

#######################################################

print("----------------------------------")

plaintext = u"defendtheeastwallofthecastle"
key = 4

print(plaintext)
enc = chipher.encrypt(plaintext, key)
print(enc)
dec = chipher.decrypt(enc, key)
print(dec)

'''
thequickbrownfoxjumpsoverthelazydog
tubnjsrldhqikrwfxupoeteayoecoomvhzg
thequickbrownfoxjumpsoverthelazydog
----------------------------------
wearediscoveredfleeatonce
wecrlteerdsoeefeaocaivden
wearediscoveredfleeatonce
----------------------------------
defendtheeastwallofthecastle
dttfsedhswotatfneaalhcleelee
defendtheeastwallofthecastle
'''
