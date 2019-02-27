#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot13 
from secretpy import CryptMachine
from secretpy.cmdecorators import *
from secretpy import alphabet

def encdec(machine, plaintext):
	print("----------------------------------")
	print(plaintext)
	enc = machine.encrypt(plaintext)
	print(enc)
	dec = machine.decrypt(enc)
	print(dec)

cm = SaveCase(CryptMachine(Rot13()))

plaintext  = u"thisisasecretmessage"
encdec(cm, plaintext)

cm = SaveSpaces(cm)

plaintext  = u"Why did the chicken cross the road Gb trg gb gur bgure fvqr"
encdec(cm, plaintext)

plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
cm.set_alphabet(alphabet.GERMAN)
encdec(cm, plaintext)

plaintext  = u"текст"
cm.set_alphabet(alphabet.RUSSIAN)
encdec(cm, plaintext)

