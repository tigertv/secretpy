#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Scytale, CryptMachine, alphabets
from secretpy.cmdecorators import SaveAll, RemoveNonAlphabet


alphabet = alphabets.GERMAN
plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = Scytale()

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


cm0 = CryptMachine(cipher, key)
cm0.set_alphabet(alphabet)

plaintext = "I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!"
cm = SaveAll(cm0)
encdec(cm, plaintext)

plaintext = "I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!"
cm = RemoveNonAlphabet(cm0)
encdec(cm, plaintext)

'''
Output:

thequickbrownfoxjumpsoverthelazydog
tqcrnxmorezohukofjpvtlygeibwousehad
thequickbrownfoxjumpsoverthelazydog
=====================================
thequickbrownfoxjumpsoverthelazydog
tqcrnxmorezohukofjpvtlygeibwousehad
thequickbrownfoxjumpsoverthelazydog
--------------------------------------------------------------------
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
I vola tac-rheeaile npbcrtseat. Ttona heh : ^,&@$~(*;?&#. Aets'r hs!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
--------------------------------------------------------------------
I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!
inonahehaeilevlfertdtvolatacrwlmeltmeolenpbcrtsiroaohga
idontlovenonalphabetcharactersiwillremoveallofthemgreat

'''
