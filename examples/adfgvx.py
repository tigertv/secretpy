#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import ADFGVX, CryptMachine


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))
    print("-------------------------------")


key = "cargo"
cm = CryptMachine(ADFGVX(), key)

alphabet = [
    u"f", u"n", u"h", u"e", u"q", u"0",
    u"r", u"d", u"z", u"o", u"c", u"9",
    u"ij", u"s", u"a", u"g", u"u", u"8",
    u"b", u"v", u"k", u"p", u"w", u"7",
    u"x", u"m", u"y", u"t", u"l", u"6",
    u"1", u"2", u"3", u"4", u"5", u".",
]
cm.set_alphabet(alphabet)
key = "battle"
plaintext = "attackatdawn11.25"
encdec(cm, plaintext)

key = "deutsch"
cm.set_key(key)
plaintext = "howstuffworks"
encdec(cm, plaintext)
