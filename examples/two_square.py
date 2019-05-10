#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import TwoSquare
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

key = (u"example", u"keyword")

cm = NoSpaces(UpperCase(CryptMachine(TwoSquare())))

cm.set_alphabet(alphabet)
cm.set_key(key)
plaintext = u"Help me Obi wan Kenobi"
encdec(cm, plaintext)

'''
Help me Obi wan Kenobi
XGDLXWSDJYRYHOTKDG
HELPMEOBIWANKENOBI
----------------------------------
'''
