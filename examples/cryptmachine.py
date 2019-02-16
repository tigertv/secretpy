#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import CryptMachine 
from secretpy import Caesar
from secretpy import Atbash 

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = Caesar()

print("-----------------------------------")

machine = CryptMachine(cipher, key);
enc = machine.encrypt(plaintext)
print(enc)
dec = machine.decrypt(enc)
print(dec)

print("-----------------------------------")

machine.setAlphabet(alphabet)
enc = machine.encrypt(plaintext)
print(enc)
dec = machine.decrypt(enc)
print(dec)

print("-----------------------------------")

machine.setKey(9)
enc = machine.encrypt(plaintext)
print(enc)
dec = machine.decrypt(enc)
print(dec)

print("-----------------------------------")

machine.setCipher(Atbash())
enc = machine.encrypt(plaintext)
print(enc)
dec = machine.decrypt(enc)
print(dec)
