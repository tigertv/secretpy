#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Atbash
from secretpy import CryptMachine

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

alphabet = u"אבגדהוזחטיךכלםמןנסעףפץצקרשת"
plaintext  = u"במקום"
cm.setAlphabet(alphabet)
encdec(cm, plaintext)

plaintext  = u"The Fox jumps in Zoo too Achtung minen"

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
cm.setAlphabet(alphabet)
encdec(cm, plaintext)

plaintext  = u"Achtung Minen"
encdec(cm, plaintext)
