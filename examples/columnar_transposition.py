#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import ColumnarTransposition, CryptMachine


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))
    print("-------------------------------")


key = "cargo"
cm = CryptMachine(ColumnarTransposition(), key)

plaintext = "attackatdawn"
encdec(cm, plaintext)

key = "deutsch"
cm.set_key(key)
plaintext = "howstuffworks"
encdec(cm, plaintext)

'''
attackatdawn
tanakwadcatt
attackatdawn
-------------------------------
howstuffworks
ushfowftksrwo
howstuffworks
-------------------------------
'''
