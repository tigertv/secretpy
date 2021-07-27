#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot47, CryptMachine
from secretpy.cmdecorators import SaveAll


def encdec(machine, plaintext):
    print("----------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)


plaintext = u"The Quick Brown Fox Jumps Over The Lazy Dog."

cm = CryptMachine(Rot47())
encdec(cm, plaintext)

cm = SaveAll(cm)
encdec(cm, plaintext)

'''
----------------------------------
The Quick Brown Fox Jumps Over The Lazy Dog.
%96"F:4<qC@H?u@IyF>AD~G6C%96{2KJs@8]
TheQuickBrownFoxJumpsOverTheLazyDog.
----------------------------------
The Quick Brown Fox Jumps Over The Lazy Dog.
%96 "F:4< qC@H? u@I yF>AD ~G6C %96 {2KJ s@8]
The Quick Brown Fox Jumps Over The Lazy Dog.
'''
