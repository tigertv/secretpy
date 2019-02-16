#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Polybius 

alphabet = [
	u"p", u"h", u"q", u"g", u"m",
	u"e", u"a", u"y", u"l", u"n", 
	u"o", u"f", u"d", u"x", u"k", 
	u"r", u"c", u"v", u"s", u"z", 
	u"w", u"b", u"u", u"t", u"ij"
]

plaintext  = u"defendtheeastwallofthecastle"
key = ""
cipher = Polybius();

print(plaintext)
enc = cipher.encrypt(key, plaintext, alphabet)
print(enc)

dec = cipher.decrypt(key, enc, alphabet) 
print(dec)


##################################################################################
print("-------------------------------")

plaintext = "sometext"

print(plaintext)
enc = cipher.encrypt(key, plaintext) 
print(enc)

dec = cipher.decrypt(key, enc) 
print(dec)

##################################################################################
print("-------------------------------")

plaintext = "thisisasecretmessage"

print(plaintext)
enc = cipher.encrypt(key, plaintext) 
print(enc)

dec = cipher.decrypt(key, enc) 
print(dec)

