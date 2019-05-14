#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import ColumnarTransposition, CryptMachine
from secretpy import alphabets


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))
    print("-------------------------------")


key = "cargo"
cm = CryptMachine(ColumnarTransposition(), key)

alphabet = alphabets.ENGLISH

cm.set_alphabet(alphabet)
plaintext = "attackatdawn"
encdec(cm, plaintext)

key = "deutsch"
cm.set_key(key)
plaintext = "howstuffworks"
encdec(cm, plaintext)

'''
attackatdawn
tanakwadzcazttz
attackatdawnzzz
-------------------------------
howstuffworks
ushfowfztksrwo
howstuffworksz
-------------------------------
'''
