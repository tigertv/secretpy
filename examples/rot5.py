#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot5
from secretpy import alphabets
from secretpy import CryptMachine


def encdec(machine, plaintext):
    print("----------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)


cm = CryptMachine(Rot5())

plaintext = alphabets.DECIMAL
encdec(cm, plaintext)
'''
----------------------------------
0123456789
5678901234
0123456789
'''
