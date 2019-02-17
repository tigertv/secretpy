#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Polybius 
from secretpy import CryptMachine

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
cm.setAlphabet(alphabet)
plaintext = "sometext"
encdec(cm, plaintext)

plaintext = "thisisasecretmessage"
encdec(cm, plaintext)

alphabet = [
	u"Α", u"Β", u"Γ", u"Δ", u"Ε", 
	u"Ζ", u"Η", u"Θ", u"Ι", u"Κ", 
	u"Λ", u"Μ", u"Ν", u"Ξ", u"Ο", 
	u"Π", u"Ρ", u"Σ", u"Τ", u"Υ", 
	u"Φ", u"Χ", u"Ψ", u"Ω"
]
cm.setAlphabet(alphabet)
plaintext = u"ΠΙΝΑΚΑΣ"
encdec(cm, plaintext)
