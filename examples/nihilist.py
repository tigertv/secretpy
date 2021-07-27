#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Nihilist, CryptMachine, alphabets as al


def encdec(cipher, plaintext, key, alphabet=al.ENGLISH):
    print(plaintext)
    enc = cipher.encrypt(plaintext, key, alphabet)
    print(enc)
    print(cipher.decrypt(enc, key, alphabet))
    print("----------------------------------")


key = "english"
plaintext = u"thequickbrownfoxjumpsoverthelazydog"
cipher = Nihilist()
encdec(cipher, plaintext, key)


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))
    print("----------------------------------")


key = "mykey"
cm = CryptMachine(cipher, key)

alphabet = (
    u"z", u"e", u"b", u"r", u"a",
    u"s", u"c", u"d", u"f", u"g",
    u"h", u"ij", u"k", u"l", u"m",
    u"n", u"o", u"p", u"q", u"t",
    u"u", u"v", u"w", u"x", u"y"
)
cm.set_alphabet(alphabet)
plaintext = u"Waltz, bad nymph, for quick jigs vex."
encdec(cm, plaintext)

alphabet = (
    u"a", u"b", u"c", u"d", u"e", u"f",
    u"g", u"h", u"i", u"j", u"k", u"l",
    u"m", u"n", u"o", u"p", u"q", u"r",
    u"s", u"t", u"u", u"v", u"w", u"x",
    u"y", u"z", u"0", u"1", u"2", u"3",
    u"4", u"5", u"6", u"7", u"8", u"9",
)
cm.set_alphabet(alphabet)
key = "freedom"
cm.set_key(key)
plaintext = u"Meet thursday 2300hr!"
encdec(cm, plaintext)

alphabet = (
    u"а", u"б", u"в", u"г", u"д", u"её",
    u"ж", u"з", u"ий", u"к", u"л", u"м",
    u"н", u"о", u"п", u"р", u"с", u"т",
    u"у", u"ф", u"х", u"ц", u"ч", u"ш",
    u"щ", u"ы", u"ьъ", u"э", u"ю", u"я",
    u"1", u"2", u"3", u"4", u"5", u"6"
)
cm.set_alphabet(alphabet)
key = u"ключ"
cm.set_key(key)
plaintext = u"текст"
encdec(cm, plaintext)

alphabet = al.GREEK
cm.set_alphabet(alphabet)
plaintext = u"ΠΙΝΑΚΑΣ"
encdec(cm, plaintext)

'''
Output:

thequickbrownfoxjumpsoverthelazydog
57 54 36 61 66 64 35 40 44 57 59 68 73 38 48 78 45 69 54 75 63 48 76 36 62 65 63 37 41 43 73 77 37 74 43
thequickbrownfoxjumpsoverthelazydog
----------------------------------
Waltz, bad nymph, for quick jigs vex.
88 70 67 57 66 48 70 56 53 110 70 98 64 36 97 49 99 84 44 77 68 87 65 37 76 87 67 87
waltzbadnymphforquickiigsvex
----------------------------------
Meet thursday 2300hr!
47 51 30 57 56 55 74 52 77 29 26 65 88 87 69 89 37 51
meetthursday2300hr
----------------------------------
текст
60 41 79 80 60
текст
----------------------------------
ΠΙΝΑΚΑΣ
95 78 87 65 79 65 97
πινακασ
----------------------------------
'''
