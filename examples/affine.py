#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Affine, alphabets


alphabet = alphabets.GERMAN
plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = [7, 8]

cipher = Affine()
print(plaintext)

enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)

#######################################################

print("----------------------------------")

key = [3, 4]
plaintext = u"attackatdawn"

# use default english alphabet
print(plaintext)
enc = cipher.encrypt(plaintext, key)
print(enc)
dec = cipher.decrypt(enc, key)
print(dec)

"""
thequickbrownfoxjumpsoverthelazydog
vögaüewsphqmjnqtlücxoqfghvögzidäßqu
thequickbrownfoxjumpsoverthelazydog
----------------------------------
attackatdawn
ejjekiejnesr
attackatdawn
"""
