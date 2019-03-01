#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Trifid
from secretpy import CryptMachine

def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))
    print("----------------------------------")

key = 5
cm = CryptMachine(Trifid(), key)

alphabet = [
    u"e", u"p", u"s", 
    u"d", u"u", u"c", 
    u"v", u"w", u"y",

    u"m", u".", u"z", 
    u"l", u"k", u"x", 
    u"n", u"b", u"t", 

    u"f", u"g", u"o", 
    u"r", u"i", u"j", 
    u"h", u"a", u"q",
]

plaintext  = u"defendtheeastwallofthecastle."
cm.set_alphabet(alphabet)
encdec(cm, plaintext)
