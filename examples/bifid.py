#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Bifid, CryptMachine, alphabets as al
from secretpy.cmdecorators import UpperCase, SaveAll, Block


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
plaintext = u"Текст здесь, много!!!"
encdec(cm, plaintext)

cm1 = Block(cm)

alphabet = [
    u"p", u"h", u"q", u"g", u"m",
    u"e", u"a", u"y", u"l", u"n",
    u"o", u"f", u"d", u"x", u"k",
    u"r", u"c", u"v", u"s", u"z",
    u"w", u"b", u"u", u"t", u"ij"
]
cm1.set_alphabet(alphabet)
plaintext = u"Defend the East Wall of the Castle!"
encdec(cm1, plaintext)

cm1 = UpperCase(cm1)
alphabet = [
    u"b", u"g", u"w", u"k", u"z",
    u"q", u"p", u"n", u"d", u"s",
    u"ij", u"o", u"a", u"x", u"e",
    u"f", u"c", u"l", u"u", u"m",
    u"t", u"h", u"y", u"v", u"r"
]
cm1.set_alphabet(alphabet)
cm1.set_key(10)
plaintext = "flee at once"
encdec(cm1, plaintext)

cm = SaveAll(cm)

alphabet = al.GREEK_SQUARE
cm.set_alphabet(alphabet)
plaintext = u"Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)"
encdec(cm, plaintext)

'''
Текст здесь, много!!!
нит4яжвыяьинтбф
текстздесьмного
----------------------------------
Defend the East Wall of the Castle!
ffyhm khycp liash adtrl hcchl blr
defendtheeastwallofthecastle
----------------------------------
flee at once
UAEOL WRINS
FLEEATONCE
----------------------------------
Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)
Ζλζπρ οεπκφ ζιν μζυτυ η κλφδζγεγφ. (Πγδαργγ Ρυτακς)
Θελει αρετη και τολμη η ελευθερια. (Ανδρεας Καλβος)
----------------------------------
'''
