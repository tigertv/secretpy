#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import CryptMachine 
from secretpy import Caesar
from secretpy import Atbash 

def encdec(machine, plaintext):
	enc = machine.encrypt(plaintext)
	print(enc)
	dec = machine.decrypt(enc)
	print(dec)
	print("-----------------------------------")

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = Caesar()

cm = CryptMachine(cipher, key)
encdec(cm, plaintext)

cm.setAlphabet(alphabet)
encdec(cm, plaintext)

cm.setKey(9)
encdec(cm, plaintext)

cm.setCipher(Atbash())
encdec(cm, plaintext)
