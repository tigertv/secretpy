#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import FourSquare
from secretpy import CryptMachine
from secretpy import alphabets
from secretpy.cmdecorators import NoSpaces, UpperCase


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)
    print("----------------------------------")


alphabet = alphabets.ENGLISH_SQUARE_OQ

key = (u"exampl", u"keyword")

cm = NoSpaces(UpperCase(CryptMachine(FourSquare())))

cm.set_alphabet(alphabet)
cm.set_key(key)
plaintext = u"Help me Obi wan Kenobi"
encdec(cm, plaintext)

alphabet = alphabets.ENGLISH_SQUARE_IJ
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
