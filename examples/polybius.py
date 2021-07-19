#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Polybius, CryptMachine, alphabets as al
from secretpy.cmdecorators import SaveAll


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)
    print("----------------------------------")


key = "mykey"
cm = CryptMachine(Polybius(), key)

plaintext = u"Defend the east wall of the castle"
encdec(cm, plaintext)

cm = SaveAll(cm)

alphabet = [
    u"p", u"h", u"q", u"g", u"m",
    u"e", u"a", u"y", u"l", u"n",
    u"o", u"f", u"d", u"x", u"k",
    u"r", u"c", u"v", u"s", u"z",
    u"w", u"b", u"u", u"t", u"ij"
]
cm.set_alphabet(alphabet)
encdec(cm, plaintext)

plaintext = "thisisasecretmessage"
encdec(cm, plaintext)

cm.set_alphabet(al.GREEK)
cm.set_key(u"πινακασ")
plaintext = u"Ξεσκεπάζω την ψυχοφθόρα σας βδελυγμία."
encdec(cm, plaintext)

'''
Defend the east wall of the castle
22142314332243251414154243461532323423432514211542433214
defendtheeastwallofthecastle
----------------------------------
Defend the east wall of the castle
341433 143 1345 4211 41 424 4454512425253233542114422444542514
defend the east wall of the castle
----------------------------------
thisisasecretmessage
5421554455442444144241145411144444242314
thisisasecretmessage
----------------------------------
Ξεσκεπάζω την ψυχοφθόρα σας βδελυγμία.
422516152 511 213161513 213 565255435.434444514161446222425365223413514
ξεσκεπάζω την ψυχοφθόρα σας βδελυγμία.
----------------------------------
'''
