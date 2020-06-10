#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Caesar, CryptMachine, alphabets
from secretpy.cmdecorators import SaveAll


alphabet = alphabets.GERMAN
plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = Caesar()

print(plaintext)
enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)

print('=====================================')

print(plaintext)
# use default english alphabet
enc = cipher.encrypt(plaintext, key)
print(enc)
dec = cipher.decrypt(enc, key)
print(dec)

# using cryptmachine

def encdec(machine, plaintext):
    print("--------------------------------------------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))


cm = SaveAll(CryptMachine(cipher, key))
cm.set_alphabet(alphabet)

plaintext = "I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!"
encdec(cm, plaintext)

'''
Output:

thequickbrownfoxjumpsoverthelazydog
wkhtxlfneurzqirämxpsvryhuwkhodüögrj
thequickbrownfoxjumpsoverthelazydog
=====================================
thequickbrownfoxjumpsoverthelazydog
wkhtxlfneurzqiramxpsvryhuwkhodcbgrj
thequickbrownfoxjumpsoverthelazydog
-------------------------------
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
L oryh qrq-doskdehw fkdudfwhuv. Wkhvh duh : ^,&@$~(*;?&#. Wkdw'v lw!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
'''
