#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Chao, CryptMachine, alphabets
from secretpy.cmdecorators import UpperCase, SaveAll


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))
    print("-------------------------------")


alphabet = "ptlnbqdeoysfavzkgjrihwxumc"  # RIGHT WHEEL PT
key = "hxuczvamdslkpefjrigtwobnyq"       # LEFT WHEEL CT

cm = UpperCase(SaveAll(CryptMachine(Chao(), key)))
cm.set_alphabet(alphabet)

plaintext = "well done is better than well said"
encdec(cm, plaintext)

plaintext = "plaintext"
encdec(cm, plaintext)

cm.set_alphabet(alphabets.ENGLISH)
cm.set_key(alphabets.ENGLISH)
plaintext = "do not use pc"
encdec(cm, plaintext)

'''
Output:

well done is better than well said
OAHQ HCNY NX TSZJRR HJBY HQKS OUJY
WELL DONE IS BETTER THAN WELL SAID
-------------------------------
plaintext
HULROKQUA
PLAINTEXT
-------------------------------
do not use pc
DN LLQ QYM MW
DO NOT USE PC
-------------------------------
'''
