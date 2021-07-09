#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot18, CryptMachine, alphabets
from secretpy.cmdecorators import SaveAll, UpperCase


def encdec(machine, plaintext):
    print("----------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)


cm = SaveAll(CryptMachine(Rot18()))

plaintext = u"The man has 536 dogs"
encdec(cm, plaintext)

plaintext = alphabets.RUSSIAN + alphabets.DECIMAL
cm.set_alphabet(alphabets.RUSSIAN)
encdec(cm, plaintext)

plaintext = u"У человека 536 собак"
encdec(cm, plaintext)

plaintext = alphabets.GREEK + " " + alphabets.DECIMAL
cm = UpperCase(cm)
cm.set_alphabet(alphabets.GREEK)
encdec(cm, plaintext)
