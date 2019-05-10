#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Nihilist
from secretpy import CryptMachine


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))
    print("----------------------------------")


key = "russian"
cm = CryptMachine(Nihilist(), key)
alphabet = [
    u"z", u"e", u"b", u"r", u"a",
    u"s", u"c", u"d", u"f", u"g",
    u"h", u"ij", u"k", u"l", u"m",
    u"n", u"o", u"p", u"q", u"t",
    u"u", u"v", u"w", u"x", u"y"
]
plaintext = u"dynamitewinterpalace"
cm.set_alphabet(alphabet)
encdec(cm, plaintext)

alphabet = [
    u"a", u"b", u"c", u"d", u"e", u"f",
    u"g", u"h", u"i", u"j", u"k", u"l",
    u"m", u"n", u"o", u"p", u"q", u"r",
    u"s", u"t", u"u", u"v", u"w", u"x",
    u"y", u"z", u"0", u"1", u"2", u"3",
    u"4", u"5", u"6", u"7", u"8", u"9",
]
key = "freedom"
plaintext = u"meetthursday2300hr"
cm.set_alphabet(alphabet)
cm.set_key(key)
encdec(cm, plaintext)

alphabet = [
    u"а", u"б", u"в", u"г", u"д", u"её",
    u"ж", u"з", u"ий", u"к", u"л", u"м",
    u"н", u"о", u"п", u"р", u"с", u"т",
    u"у", u"ф", u"х", u"ц", u"ч", u"ш",
    u"щ", u"ы", u"ьъ", u"э", u"ю", u"я",
    u"1", u"2", u"3", u"4", u"5", u"6"
]

cm.set_alphabet(alphabet)
key = u"ключ"
plaintext = u"текст"
encdec(cm, plaintext)

alphabet = [
    u"Α", u"Β", u"Γ", u"Δ", u"Ε",
    u"Ζ", u"Η", u"Θ", u"Ι", u"Κ",
    u"Λ", u"Μ", u"Ν", u"Ξ", u"Ο",
    u"Π", u"Ρ", u"Σ", u"Τ", u"Υ",
    u"Φ", u"Χ", u"Ψ", u"Ω"
]
plaintext = u"ΠΙΝΑΚΑΣ"
cm.set_alphabet(alphabet)
encdec(cm, plaintext)

'''
Output:

dynamitewinterpalace
37 106 62 36 67 47 86 26 104 53 62 77 27 55 57 66 55 36 54 27
dynamitewinterpalace
----------------------------------
meetthursday2300hr
47 51 30 57 56 55 74 52 77 29 26 65 88 87 69 89 37 51
meetthursday2300hr
----------------------------------
текст
102 82 90 101 102
текст
----------------------------------
ΠΙΝΑΚΑΣ
95 78 87 65 79 65 97
ΠΙΝΑΚΑΣ
----------------------------------
'''
