#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot18
from secretpy import CryptMachine
from secretpy.cmdecorators import SaveCase, SaveSpaces, UpperCase
from secretpy import alphabet


def encdec(machine, plaintext):
    print("----------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)


cm = SaveCase(SaveSpaces(CryptMachine(Rot18())))

plaintext = u"The man has 536 dogs"
encdec(cm, plaintext)

plaintext = alphabet.RUSSIAN + alphabet.DECIMAL
cm.set_alphabet(alphabet.RUSSIAN)
encdec(cm, plaintext)

plaintext = u"У человека 536 собак"
encdec(cm, plaintext)

plaintext = alphabet.GREEK + " " + alphabet.DECIMAL
cm = UpperCase(cm)
cm.set_alphabet(alphabet.GREEK)
encdec(cm, plaintext)
