#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Bazeries, CryptMachine, alphabets
from secretpy.cmdecorators import UpperCase


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)
    print("----------------------------------")


alphabet = alphabets.ENGLISH_SQUARE_IJ

key = (81257, u"eightyonethousandtwohundredfiftyseven")

cm = UpperCase(CryptMachine(Bazeries()))

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
