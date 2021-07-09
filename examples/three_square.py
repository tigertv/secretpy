#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import ThreeSquare, CryptMachine, alphabets
from secretpy.cmdecorators import UpperCase


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)
    print("----------------------------------")


alphabet = alphabets.ENGLISH_SQUARE_OQ
key = (u"example", u"keyword", u"third")
cm = UpperCase(CryptMachine(ThreeSquare()))
cm.set_alphabet(alphabet)
cm.set_key(key)
plaintext = u"Help me Obi wan Kenobi"
encdec(cm, plaintext)

alphabet = alphabets.ENGLISH_SQUARE_IJ
cm.set_alphabet(alphabet)
key = (u"criptog", u"segurt", u"mars")
cm.set_key(key)
plaintext = u"attack at dawn"
encdec(cm, plaintext)

'''
Help me Obi wan Kenobi
HJKNEMDHOHSACLYRISFJKUUKBEF
HELPMEOBIWANKENOBI
----------------------------------
attack at dawn
QCTZABCSKXCATDAFWN
ATTACKATDAWN
----------------------------------
'''
