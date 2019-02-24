#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot5
from secretpy import CryptMachine
from secretpy.cmdecorators import *

def encdec(machine, plaintext):
	print("----------------------------------")
	print(plaintext)
	enc = machine.encrypt(plaintext)
	print(enc)
	dec = machine.decrypt(enc)
	print(dec)

cm = CryptMachine(Rot5())

plaintext  = u"0123456789"
encdec(cm, plaintext)

