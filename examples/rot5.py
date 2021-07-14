#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot5, alphabets, CryptMachine


def encdec(machine, plaintext):
    print("----------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)


cm = CryptMachine(Rot5())

plaintext = "My text " + alphabets.DECIMAL + " your text"
encdec(cm, plaintext)

'''
----------------------------------
My text 0123456789 your text
5678901234
0123456789
'''
