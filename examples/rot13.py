#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot13 
from secretpy import CryptMachine
from secretpy.cmdecorators import *

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

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
cm.setAlphabet(alphabet)
encdec(cm, plaintext)

alphabet = u"абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
plaintext  = u"текст"
cm.setAlphabet(alphabet)
encdec(cm, plaintext)

