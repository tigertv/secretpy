#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot13, Caesar, CryptMachine, CompositeMachine
from secretpy.cmdecorators import SaveAll


def encdec(machine, plaintext):
    print("=======================================")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)


key = 5
plaintext = u"Dog jumps four times and cat six times"
print(plaintext)

cm1 = SaveAll(CryptMachine(Caesar(), key))
enc = cm1.encrypt(plaintext)
print(enc)

cm2 = SaveAll(CryptMachine(Rot13()))
enc = cm2.encrypt(enc)
print(enc)

print("=======================================")

cm = CompositeMachine(cm1)
cm.add_machines(cm2)
enc = cm.encrypt(plaintext)
print(enc)
encdec(cm, plaintext)

cm.add_machines(cm1, cm2)
encdec(cm, plaintext)

'''
Output:

Dog jumps four times and cat six times
Itl ozrux ktzw ynrjx fsi hfy xnc ynrjx
Vgy bmehk xgmj laewk sfv usl kap laewk
=======================================
Vgy bmehk xgmj laewk sfv usl kap laewk
=======================================
Dog jumps four times and cat six times
Vgy bmehk xgmj laewk sfv usl kap laewk
Dog jumps four times and cat six times
=======================================
Dog jumps four times and cat six times
Nyq tewzc pyeb dswoc kxn mkd csh dswoc
Dog jumps four times and cat six times

'''
