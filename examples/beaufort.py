#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import CryptMachine 
from secretpy import Beaufort 

plaintext  = u"helloworld"
key = "key"

cm = CryptMachine(Beaufort(), key)

print(plaintext)
enc = cm.encrypt(plaintext)
print(enc)
dec = cm.decrypt(enc)
print(dec)

print("-----------------------------------")

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
cm.setAlphabet(alphabet)

print(plaintext)
enc = cm.encrypt(plaintext)
print(enc)
dec = cm.decrypt(enc)
print(dec)

