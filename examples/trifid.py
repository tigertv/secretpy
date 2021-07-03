#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Trifid, CryptMachine
from secretpy.cmdecorators import RemoveNonAlphabet, SaveAll


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))
    print("----------------------------------")


key = 5
cm = CryptMachine(Trifid(), key)

alphabet = u"epsducvwym.zlkxnbtfgorijhaq"  # 27 characters
cm.set_alphabet(alphabet)

plaintext = u"defendtheeastwallofthecastle"
encdec(cm, plaintext)

cm1 = RemoveNonAlphabet(cm)
alphabet = (
    u"aåä", u"b", u"c",
    u"d", u"e",  u"f",
    u"g", u"h", u"i",

    u"j", u"k", u"l",
    u"m", u"n", u"oö",
    u"p", u"q", u"r",

    u"s", u"t", u"u",
    u"v", u"w", u"x",
    u"y", u"z", u"+",
)
cm1.set_alphabet(alphabet)

plaintext = u"Flygande bäckasiner söka hwila på mjuka tuvor!"
encdec(cm1, plaintext)

cm2 = SaveAll(cm)
alphabet = "felixmardstbcghjknopquvwyz+"
cm2.set_alphabet(alphabet)

plaintext = u"Aide-toi, le ciel t'aidera"
encdec(cm2, plaintext)


'''
defendtheeastwallofthecastle
suefecphsegyyjiximfofocejlrf
defendtheeastwallofthecastle
----------------------------------
Flygande bäckasiner söka hwila på mjuka tuvor!
fbiiajbmdmdsazckwpnujshvokdgpaqgackzkri
flygandebackasinersokahwilapamjukatuvor
----------------------------------
Aide-toi, le ciel t'aidera
Fmjf-voi, ss uftf p'ufeqqc
Aide-toi, le ciel t'aidera
----------------------------------
'''
