#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import FourSquare
from secretpy import CryptMachine
from secretpy.cmdecorators import NoSpaces, UpperCase


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)
    print("----------------------------------")


alphabet = (
    u"a", u"b", u"c", u"d", u"e",
    u"f", u"g", u"h", u"i", u"j",
    u"k", u"l", u"m", u"n", u"oq",
    u"p", u"r", u"s", u"t", u"u",
    u"v", u"w", u"x", u"y", u"z",
)

key = (u"exampl", u"keyword")

cm = NoSpaces(UpperCase(CryptMachine(FourSquare())))

cm.set_alphabet(alphabet)
cm.set_key(key)
plaintext = u"Help me Obi wan Kenobi"
encdec(cm, plaintext)

alphabet = (
    u"a", u"b", u"c", u"d", u"e",
    u"f", u"g", u"h", u"ij", u"k",
    u"l", u"m", u"n", u"o", u"p",
    u"q",  u"r", u"s", u"t", u"u",
    u"v", u"w", u"x", u"y", u"z",
)
cm.set_alphabet(alphabet)
key = (u"criptog", u"segurt")
cm.set_key(key)
plaintext = u"attack at dawn"
encdec(cm, plaintext)

'''
Help me Obi wan Kenobi
FYGMKYHOBXMFKKKIMD
HELPMEOBIWANKENOBI
----------------------------------
attack at dawn
PMMUTBPMCUXH
ATTACKATDAWN
----------------------------------
'''
