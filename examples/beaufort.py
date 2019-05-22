#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import CryptMachine
from secretpy import Beaufort
from secretpy import alphabets

plaintext = u"helloworld"
key = "key"

cm = CryptMachine(Beaufort(), key)

print(plaintext)
enc = cm.encrypt(plaintext)
print(enc)
dec = cm.decrypt(enc)
print(dec)

print("-----------------------------------")

alphabet = alphabets.GERMAN
cm.set_alphabet(alphabet)

print(plaintext)
enc = cm.encrypt(plaintext)
print(enc)
dec = cm.decrypt(enc)
print(dec)

'''
helloworld
danzqcwnnh
helloworld
-----------------------------------
helloworld
danßucärnh
helloworld
'''
