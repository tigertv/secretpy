#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Atbash, CryptMachine, alphabets
import secretpy.cmdecorators as md


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)
    print("----------------------------------")


cm = CryptMachine(Atbash())
cm = md.UpperCase(cm)

plaintext = u"attackatdawn"
encdec(cm, plaintext)

plaintext = u"במקום"
cm.set_alphabet(alphabets.HEBREW)
encdec(cm, plaintext)

plaintext = u"The Fox jumps in Zoo too Achtung minen"
cm.set_alphabet(alphabets.GERMAN)
encdec(cm, plaintext)

plaintext = u"Achtung Minen"
encdec(cm, plaintext)

cm.set_alphabet(alphabets.ARABIC)
plaintext = u"قط"
encdec(cm, plaintext)
