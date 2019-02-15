#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import ADFGX

alphabet = [u"b", u"t", u"a", u"l", u"p", u"d", u"h", u"o", u"z", u"k", u"q", u"f", u"v", u"s", u"n", u"g", u"ij", u"c", u"u", u"x", u"m", u"r", u"e", u"w", u"y"]
plaintext  = u"attackatonce"
key = "cargo"
chipher = ADFGX();

print(plaintext)
enc = chipher.encrypt(key, plaintext, alphabet)
print(enc)

dec = chipher.decrypt(key, enc, alphabet)
print(dec)

##################################################################################
print("-------------------------------")

alphabet = [
	u"f", u"n", u"h", u"e", u"q",
	u"r", u"d", u"z", u"o", u"c", 
	u"ij", u"s", u"a", u"g", u"u", 
	u"b", u"v", u"k", u"p", u"w", 
	u"x", u"m", u"y", u"t", u"l"
]
key = "battle"
plaintext = "attackatdawn"

print(plaintext)
enc = chipher.encrypt(key, plaintext, alphabet)
print(enc)

dec = chipher.decrypt(key, enc, alphabet)
print(dec)

##################################################################################
print("-------------------------------")

key = "deutsch"
plaintext = "howstuffworks"

# use default english alphabet 5x5
print(plaintext)
enc = chipher.encrypt(key, plaintext)
print(enc)

dec = chipher.decrypt(key, enc)
print(dec)

