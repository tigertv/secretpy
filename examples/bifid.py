#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Bifid, CryptMachine, alphabets


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))
    print("----------------------------------")


key = 5
cm = CryptMachine(Bifid(), key)
alphabet = [
    u"а", u"б", u"в", u"г", u"д", u"её",
    u"ж", u"з", u"ий", u"к", u"л", u"м",
    u"н", u"о", u"п", u"р", u"с", u"т",
    u"у", u"ф", u"х", u"ц", u"ч", u"ш",
    u"щ", u"ы", u"ьъ", u"э", u"ю", u"я",
    u"1", u"2", u"3", u"4", u"5", u"6"
]
cm.set_alphabet(alphabet)
plaintext = u"текст"
encdec(cm, plaintext)

alphabet = [
    u"p", u"h", u"q", u"g", u"m",
    u"e", u"a", u"y", u"l", u"n",
    u"o", u"f", u"d", u"x", u"k",
    u"r", u"c", u"v", u"s", u"z",
    u"w", u"b", u"u", u"t", u"ij"
]
cm.set_alphabet(alphabet)
plaintext = u"defendtheeastwallofthecastle"
encdec(cm, plaintext)

alphabet = [
    u"b", u"g", u"w", u"k", u"z",
    u"q", u"p", u"n", u"d", u"s",
    u"ij", u"o", u"a", u"x", u"e",
    u"f", u"c", u"l", u"u", u"m",
    u"t", u"h", u"y", u"v", u"r"
]
cm.set_alphabet(alphabet)
cm.set_key(10)
plaintext = "fleeatonce"
encdec(cm, plaintext)

alphabet = alphabets.GREEK.upper()
plaintext = u"ΠΙΝΑΚΑΣ"
cm.set_alphabet(alphabet)
encdec(cm, plaintext)

'''
текст
нит4я
текст
----------------------------------
defendtheeastwallofthecastle
ffyhmkhycpliashadtrlhcchlblr
defendtheeastwallofthecastle
----------------------------------
fleeatonce
uaeolwrins
fleeatonce
----------------------------------
ΠΙΝΑΚΑΣ
ΡΛΖΠΣΕΓ
ΠΙΝΑΚΑΣ
----------------------------------
'''
