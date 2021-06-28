#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import TwoSquare, CryptMachine, alphabets
from secretpy.cmdecorators import RemoveNonAlphabet, UpperCase


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)
    print("----------------------------------")


alphabet = alphabets.ENGLISH_SQUARE_OQ

key = (u"example", u"keyword")

cm = UpperCase(RemoveNonAlphabet(CryptMachine(TwoSquare())))

cm.set_alphabet(alphabet)
cm.set_key(key)
plaintext = u"Help me Obi wan Kenobi"
encdec(cm, plaintext)

plaintext = u"Help me Obi wan Kenobi y"
encdec(cm, plaintext)

'''
Help me Obi wan Kenobi
XGDLXWSDJYRYHOTKDG
HELPMEOBIWANKENOBI
----------------------------------
Help me Obi wan Kenobi y
XGDLXWSDJYRYHOTKDGZX
HELPMEOBIWANKENOBIYZ
----------------------------------
'''
