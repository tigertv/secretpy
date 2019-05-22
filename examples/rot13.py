#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot13
from secretpy import CryptMachine
from secretpy.cmdecorators import SaveCase, SaveSpaces
from secretpy import alphabets


def encdec(machine, plaintext):
    print("----------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)


cm = SaveCase(CryptMachine(Rot13()))

plaintext = u"thisisasecretmessage"
encdec(cm, plaintext)

cm = SaveSpaces(cm)

plaintext = u"Why did the chicken cross the road Gb trg gb gur bgure fvqr"
encdec(cm, plaintext)

plaintext = u"thequickbrownfoxjumpsoverthelazydog"
cm.set_alphabet(alphabets.GERMAN)
encdec(cm, plaintext)

plaintext = u"текст"
cm.set_alphabet(alphabets.RUSSIAN)
encdec(cm, plaintext)
