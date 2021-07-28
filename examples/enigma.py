#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Enigma, CryptMachine, alphabets as al
from secretpy.cmdecorators import SaveAll, Block, UpperCase


def encdec(cipher, plaintext, key, alphabet=al.ENGLISH):
    print('=' * 80)
    print(plaintext)
    enc = cipher.encrypt(plaintext, key, alphabet)
    print(enc)
    print(cipher.decrypt(enc, key, alphabet))


cipher = Enigma()
key = {
    'reflector': 'B',
    'rotor_offsets': ('y', 'w', 'x'),  # Grundstellung
    'ring_offsets': ('p', 'z', 'n'),   # Ringstellung
    'rotor_order': (1, 2, 3),
    'steckers': [('a', 'e'), ('z', 'r'), ('y', 'f'), ('k', 'c')]
}

alphabet = al.ENGLISH
plaintext = u"a" * 45
encdec(cipher, plaintext, key, alphabet)

# using cryptmachine


def encdec(machine, plaintext):
    print('-' * 80)
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))


cm0 = CryptMachine(cipher, key)

cm = cm0
plaintext = "I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!"
encdec(cm, plaintext)

cm = UpperCase(Block(cm, length=5, sep="-"))
plaintext = "This text is divided by blocks of length 5!"
encdec(cm, plaintext)

cm = SaveAll(cm0)
plaintext = "I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!"
encdec(cm, plaintext)


'''
================================================================================
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
uwmmfkclcsqbwssepjlncolndnmlgulxemxrlmmconlrw
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
--------------------------------------------------------------------------------
I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!
keqceemxifxtwwogpmtxaslpdverbdoloqzapagjpnaxzldgaajxodo
idontlovenonalphabetcharactersiwillremoveallofthemgreat
--------------------------------------------------------------------------------
This text is divided by blocks of length 5!
GTNRE-LJWEA-IDZJH-ANMDV-EAXMJ-IBAMR-PEB
THISTEXTISDIVIDEDBYBLOCKSOFLENGTH
--------------------------------------------------------------------------------
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
K vqgt gmy-curewrbj hqlqcydwbx. Ecmdc xsb : ^,&@$~(*;?&#. Ojlf'b bf!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
'''
