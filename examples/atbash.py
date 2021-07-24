#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Atbash, CryptMachine, alphabets
from secretpy.cmdecorators import UpperCase, SaveAll


def encdec(machine, plaintext):
    print("-" * 80)
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)


cm = UpperCase(CryptMachine(Atbash()))

plaintext = u"attackatdawn"
encdec(cm, plaintext)

plaintext = u"במקום"
cm.set_alphabet(alphabets.HEBREW)
encdec(cm, plaintext)

cm = SaveAll(cm)
plaintext = u"The quick brown fox jumps over the lazy dog."
cm.set_alphabet(alphabets.GERMAN)
encdec(cm, plaintext)

plaintext = u"Achtung Minen!!!"
encdec(cm, plaintext)

cm.set_alphabet(alphabets.ARABIC)
plaintext = u"حريتي : أن أكون كما لا يريدون لي أن أكون"
encdec(cm, plaintext)

'''
--------------------------------------------------------------------------------
attackatdawn
ZGGZXPZGWZDM
ATTACKATDAWN
--------------------------------------------------------------------------------
במקום
שלדץם
במקום
--------------------------------------------------------------------------------
The quick brown fox jumps over the lazy dog.
KWZ NJVÖT ÜMPHQ YPG UJROL PIZM KWZ SßEF ÄPX.
THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
--------------------------------------------------------------------------------
Achtung Minen!!!
ßÖWKJQX RVQZQ!!!
ACHTUNG MINEN!!!
--------------------------------------------------------------------------------
حريتي : أن أكون كما لا يريدون لي أن أكون
شطقزق : غس غصثس صعا فا قطقذثس فق غس غصثس
حريتي : أن أكون كما لا يريدون لي أن أكون
'''
