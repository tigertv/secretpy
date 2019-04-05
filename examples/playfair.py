#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Playfair
from secretpy import CryptMachine
from secretpy.cmdecorators import NoSpaces, UpperCase


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)
    print("----------------------------------")


cm = NoSpaces(UpperCase(CryptMachine(Playfair())))
alphabet = [
    u"p", u"l", u"a", u"y", u"f",
    u"i", u"r", u"e", u"x", u"m",
    u"b", u"c", u"d", u"g", u"h",
    u"k", u"n", u"o", u"q", u"s",
    u"t", u"u", u"v", u"w", u"z",
]
cm.set_alphabet(alphabet)
plaintext = u"Hide the gold in the tree stump"
encdec(cm, plaintext)

plaintext = "sometext"
encdec(cm, plaintext)

plaintext = "this is a secret message"
encdec(cm, plaintext)
