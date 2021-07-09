#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import CaesarProgressive, CryptMachine, alphabets as al
from secretpy.cmdecorators import SaveAll


def encdec(cipher, plaintext, key, alphabet=al.ENGLISH):
    print('========================================================================================')
    print(plaintext)
    enc = cipher.encrypt(plaintext, key, alphabet)
    print(enc)
    print(cipher.decrypt(enc, key, alphabet))


plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = CaesarProgressive()

encdec(cipher, plaintext, key)

alphabet = al.GERMAN
plaintext = u"schweißgequältvomödentextzürnttypografjakob"
encdec(cipher, plaintext, key, alphabet)

alphabet = al.SWEDISH
plaintext = u"faqomschweizklövdutrångpjäxby"
encdec(cipher, plaintext, key, alphabet)

# using cryptmachine


def encdec(machine, plaintext):
    print("--------------------------------------------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))


cm0 = CryptMachine(cipher, key)

plaintext = "I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!"
cm = SaveAll(cm0)
encdec(cm, plaintext)

cm.set_alphabet(al.ENGLISH_SQUARE_IJ)
plaintext = "Jj becomes Ii because we use ENGLISH_SQUARE_IJ!"
encdec(cm, plaintext)

cm.set_alphabet(al.JAPANESE_HIRAGANA)
cm.set_key(1)
plaintext = u"text あい だやぎへぐゆぢ"
encdec(cm, plaintext)

plaintext = "I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!"
cm = cm0
cm.set_alphabet(al.ENGLISH)
encdec(cm, plaintext)

'''
Output:

========================================================================================
thequickbrownfoxjumpsoverthelazydog
wljwbqlumdbkcvfpcohlpmuesvkiqgggmyr
thequickbrownfoxjumpsoverthelazydog
========================================================================================
schweißgequältvomödentextzürnttypografjakob
vgmülqiqpüdkäficbryägnßtqxörovwüuunzjpumxüq
schweißgequältvomödentextzürnttypografjakob
========================================================================================
faqomschweizklövdutrångpjäxby
ievutålreqvkzäqkwllkuicmhåxcå
faqomschweizklövdutrångpjäxby
--------------------------------------------------------------------
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
L ptbl vxx-lxcvprvl vbvnxasesu. Wljyl iao : ^,&@$~(*;?&#. Etnh'h yk!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
--------------------------------------------------------------------
Jj becomes Ii because we use ENGLISH_SQUARE_IJ!
Mn glkwvpd Vw qutsnmz sb sre FPKPOYP_AZEMDS_XY!
Ii becomes Ii because we use ENGLISH_SQUARE_II!
--------------------------------------------------------------------
text あい だやぎへぐゆぢ
text いえ でりしぼそをは
text あい だやぎへぐゆぢ
--------------------------------------------------------------------
I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!
jfrryrvdnxzznzexrtxnxdxpzcuguwncptubpybjtqcdhzodbkfrfcw
idontlovenonalphabetcharactersiwillremoveallofthemgreat
'''
