#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot47, CryptMachine
from secretpy.cmdecorators import SaveAll


def encdec(machine, plaintext):
    print("----------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)


cm = SaveAll(CryptMachine(Rot47()))

plaintext = u"The man has 536 dogs!"
encdec(cm, plaintext)
