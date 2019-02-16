#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import CryptMachine 
from secretpy import Beaufort 

plaintext  = u"helloworld"
key = "key"

machine = CryptMachine(Beaufort(), key)

print(plaintext)
enc = machine.encrypt(plaintext)
print(enc)
dec = machine.decrypt(enc)
print(dec)

print("-----------------------------------")

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
machine.setAlphabet(alphabet)

print(plaintext)
enc = machine.encrypt(plaintext)
print(enc)
dec = machine.decrypt(enc)
print(dec)

