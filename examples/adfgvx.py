#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import ADFGVX, CryptMachine
from secretpy.cmdecorators import Block, UpperCase


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))
    print("-------------------------------")


key = "privacy"
cm = UpperCase(Block(CryptMachine(ADFGVX(), key), 4))

alphabet = (
    u"n", u"a", u"1", u"c", u"3", u"h",
    u"8", u"t", u"b", u"2", u"o", u"m",
    u"e", u"5", u"w", u"r", u"p", u"d",
    u"4", u"f", u"6", u"g", u"7", u"i",
    u"9", u"j", u"0", u"k", u"l", u"q",
    u"s", u"u", u"v", u"x", u"y", u"z",
)
cm.set_alphabet(alphabet)
plaintext = "Attack at 12.00am!"
encdec(cm, plaintext)

key = "pangram"
cm.set_key(key)
plaintext = "The quick brown fox jumps over the lazy dog."
encdec(cm, plaintext)

alphabet = (
    u"5", u"б", u"в", u"г", u"д", u"её",
    u"ж", u"з", u"ий", u"к", u"л", u"м",
    u"н", u"о", u"п", u"р", u"с", u"т",
    u"у", u"ф", u"х", u"ц", u"ч", u"ш",
    u"щ", u"ы", u"ьъ", u"э", u"ю", u"я",
    u"0", u"1", u"2", u"3", u"4", u"а",
)
cm.set_alphabet(alphabet)
key = "russian"
cm.set_key(key)
plaintext = u"Эй, жлоб! Где туз? Прячь юных съёмщиц в шкаф."
encdec(cm, plaintext)

'''
Attack at 12.00am!
DGDD DAGD DGAF ADDF DADV DVFA ADVX
ATTACKAT1200AM
-------------------------------
The quick brown fox jumps over the lazy dog.
DXGF VDVD VFAA GGDX AFXG XGFA GFFA DDVG DDXA FAXG ADDF XXXD AXDX VVDD DGVV FXFA VVFX XV
THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG
-------------------------------
Эй, жлоб! Где туз? Прячь юных съёмщиц в шкаф.
AAXF FGXG GDDF FVDA FDDG GGVF DGXV VAAV VFXA XDDA DGAV AGDF AXFV VFDX GFVD XFVV FG
ЭИЖЛОБГДЕТУЗПРЯЧЬЮНЫХСЬЕМЩИЦВШКАФ
-------------------------------
'''
