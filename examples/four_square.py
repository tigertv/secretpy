#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import FourSquare, CryptMachine, alphabets
from secretpy.cmdecorators import UpperCase


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)
    print("----------------------------------")


alphabet = alphabets.ENGLISH_SQUARE_OQ

key = (u"example", u"keyword")

cm = UpperCase(CryptMachine(FourSquare()))

cm.set_alphabet(alphabet)
cm.set_key(key)
plaintext = u"Help me Obi wan Kenobi"
encdec(cm, plaintext)

plaintext = u"Help me Obi wan Kenobi a"
encdec(cm, plaintext)

alphabet = alphabets.ENGLISH_SQUARE_IJ
cm.set_alphabet(alphabet)
key = (u"criptog", u"segurt")
cm.set_key(key)
plaintext = u"Attack at dawn!"
encdec(cm, plaintext)


'''
Help me Obi wan Kenobi
FYGMKYHOBXMFKKKIMD
HELPMEOBIWANKENOBI
----------------------------------
Help me Obi wan Kenobi a
FYGMKYHOBXMFKKKIMDPT
HELPMEOBIWANKENOBIAZ
----------------------------------
Attack at dawn!
PMMUTBPMCUXH
ATTACKATDAWN
----------------------------------
'''
