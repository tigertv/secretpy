#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot18, CryptMachine
from secretpy.cmdecorators import SaveAll, UpperCase, Block


def encdec(machine, plaintext):
    print("----------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)


plaintext = u"The man has 536 dogs! How many dogs do you have?"

cm = CryptMachine(Rot18())
encdec(cm, plaintext)

cm1 = Block(cm)
encdec(cm1, plaintext)

cm = SaveAll(cm)
encdec(cm, plaintext)

cm = UpperCase(cm)
encdec(cm, plaintext)

'''
----------------------------------
The man has 536 dogs! How many dogs do you have?
gurznaunf081qbtfubjznalqbtfqblbhunir
themanhas536dogshowmanydogsdoyouhave
----------------------------------
The man has 536 dogs! How many dogs do you have?
gurzn aunf0 81qbt fubjz nalqb tfqbl bhuni r
themanhas536dogshowmanydogsdoyouhave
----------------------------------
The man has 536 dogs! How many dogs do you have?
Gur zna unf 081 qbtf! Ubj znal qbtf qb lbh unir?
The man has 536 dogs! How many dogs do you have?
----------------------------------
The man has 536 dogs! How many dogs do you have?
GUR ZNA UNF 081 QBTF! UBJ ZNAL QBTF QB LBH UNIR?
THE MAN HAS 536 DOGS! HOW MANY DOGS DO YOU HAVE?
'''
