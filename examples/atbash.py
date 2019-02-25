#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Atbash
from secretpy import CryptMachine
from secretpy import alphabet
import secretpy.cmdecorators as md

def encdec(machine, plaintext):
	print(plaintext)
	enc = cm.encrypt(plaintext)
	print(enc)
	dec = cm.decrypt(enc)
	print(dec)
	print("----------------------------------")

cm = CryptMachine(Atbash())
cm = md.NoSpaces(md.UpperCase(cm))

plaintext  = u"attackatdawn"
encdec(cm, plaintext)

plaintext  = u"במקום"
cm.setAlphabet(alphabet.HEBREW)
encdec(cm, plaintext)

plaintext  = u"The Fox jumps in Zoo too Achtung minen"
cm.setAlphabet(alphabet.GERMAN)
encdec(cm, plaintext)

plaintext  = u"Achtung Minen"
encdec(cm, plaintext)

cm.setAlphabet(alphabet.ARABIC)
plaintext  = u"قط"
encdec(cm, plaintext)
