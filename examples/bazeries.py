#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Bazeries
from secretpy import CryptMachine
from secretpy.cmdecorators import NoSpaces, UpperCase


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)
    print("----------------------------------")


alphabet = (
    u"a", u"b", u"c", u"d", u"e",
    u"f", u"g", u"h", u"ij", u"k",
    u"l", u"m", u"n", u"o", u"p",
    u"q", u"r", u"s", u"t", u"u",
    u"v", u"w", u"x", u"y", u"z"
)

key = (81257, u"eightyonethousandtwohundredfiftyseven")

cm = NoSpaces(UpperCase(CryptMachine(Bazeries())))

cm.set_alphabet(alphabet)
cm.set_key(key)
plaintext = u"Whoever has made a voyage up the Hudson" \
            u" must remember the Kaatskill mountains"
encdec(cm, plaintext)

'''
Whoever has made a voyage up the Hudson must remember the Kaatskill mountains
DUMTMCDSENRTEMVEQXMOELCCRVXDMDKWXNNMUKRDKUMYNMBPRKEEPMGNGEKWXCRWB
WHOEVERHASMADEAVOYAGEUPTHEHUDSONMUSTREMEMBERTHEKAATSKILLMOUNTAINS
----------------------------------
'''
