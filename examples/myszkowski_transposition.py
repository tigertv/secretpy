#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import MyszkowskiTransposition, CryptMachine
from secretpy import alphabets


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))
    print("-------------------------------")


key = "tomato"
cm = CryptMachine(MyszkowskiTransposition(), key)

alphabet = alphabets.ENGLISH

cm.set_alphabet(alphabet)
plaintext = "wearediscoveredfleeatonce"
encdec(cm, plaintext)

'''
wearediscoveredfleeatonce
rofoacdtedseeeacweivrlene
wearediscoveredfleeatonce
-------------------------------
'''
