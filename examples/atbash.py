#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Atbash
from secretpy import CryptMachine

def encdec(machine, plaintext):
	print(plaintext)
	enc = cm.encrypt(plaintext)
	print(enc)
	dec = cm.decrypt(enc)
	print(dec)
	print("----------------------------------")

cm = CryptMachine(Atbash())

plaintext  = u"attackatdawn"
encdec(cm, plaintext)

alphabet = u"אבגדהוזחטיךכלםמןנסעףפץצקרשת"
plaintext  = u"במקום"
cm.setAlphabet(alphabet)
encdec(cm, plaintext)

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"Achtung Minen"
cm.setAlphabet(alphabet)
cm.setUpperCase()
cm.setRemoveSpaces()
encdec(cm, plaintext)
