#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Polybius 
from secretpy import CryptMachine
from secretpy.cmdecorators import *
import secretpy.alphabet as alph

def encdec(machine, plaintext):
	print(plaintext)
	enc = cm.encrypt(plaintext)
	print(enc)
	dec = cm.decrypt(enc)
	print(dec)
	print("----------------------------------")

cm = CryptMachine(Polybius())

plaintext  = u"defendtheeastwallofthecastle"
encdec(cm, plaintext)

alphabet = [
	u"p", u"h", u"q", u"g", u"m",
	u"e", u"a", u"y", u"l", u"n", 
	u"o", u"f", u"d", u"x", u"k", 
	u"r", u"c", u"v", u"s", u"z", 
	u"w", u"b", u"u", u"t", u"ij"
]
cm.set_alphabet(alphabet)
plaintext = "sometext"
encdec(cm, plaintext)

plaintext = "thisisasecretmessage"
encdec(cm, plaintext)

cm.set_alphabet(alph.GREEK)
plaintext = u"ΠΙΝΑΚΑΣ"
cm = LowerCase(cm)
encdec(cm, plaintext)
