#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Vic
from secretpy import CryptMachine


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))
    print("----------------------------------")


key = "0452"
cm = CryptMachine(Vic(), key)
alphabet = [
    u"e", u"t", u"", u"a", u"o", u"n", u"", u"r", u"i", u"s",
    u"b", u"c", u"d", u"f", u"g", u"h", u"j", u"k", u"l", u"m",
    u"p", u"q", u"/", u"u", u"v", u"w", u"x", u"y", u"z", u".",
]
plaintext = u"attackatdawn"
cm.set_alphabet(alphabet)
encdec(cm, plaintext)

'''
Output:

attackatdawn
anwhrsanroaeer
attackatdawn
----------------------------------
'''
