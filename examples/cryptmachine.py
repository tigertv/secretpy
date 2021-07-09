#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Atbash, Caesar, CryptMachine, alphabets
from secretpy.cmdecorators import SaveAll


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)
    print("-----------------------------------")


plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = Caesar()

cm = CryptMachine(cipher, key)
encdec(cm, plaintext)

cm.set_alphabet(alphabets.GERMAN)
encdec(cm, plaintext)

cm1 = SaveAll(cm)
cm1.set_key(9)
plaintext = u"the quick brown fox jumps over the lazy dog"
encdec(cm1, plaintext)

cm2 = cm
cm2.set_cipher(Atbash())
plaintext = u"Achtung Minen"
encdec(cm2, plaintext)


'''
Output:

thequickbrownfoxjumpsoverthelazydog
wkhtxlfneurzqiramxpsvryhuwkhodcbgrj
thequickbrownfoxjumpsoverthelazydog
-----------------------------------
thequickbrownfoxjumpsoverthelazydog
wkhtxlfneurzqirämxpsvryhuwkhodüögrj
thequickbrownfoxjumpsoverthelazydog
-----------------------------------
the quick brown fox jumps over the lazy dog
üqn zßrlt käxbw oxc sßvyö xanä üqn ujed mxp
the quick brown fox jumps over the lazy dog
-----------------------------------
Achtung Minen
ßöwkjqxrvqzq
achtungminen
-----------------------------------
'''
