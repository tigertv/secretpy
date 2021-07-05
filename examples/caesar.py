#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Caesar, CryptMachine, alphabets as al
from secretpy.cmdecorators import SaveAll, RemoveNonAlphabet, Block


def encdec(cipher, plaintext, key, alphabet=al.ENGLISH):
    print('========================================================================================')
    print(plaintext)
    enc = cipher.encrypt(plaintext, key, alphabet)
    print(enc)
    print(cipher.decrypt(enc, key, alphabet))


key = 3
cipher = Caesar()

plaintext = u"thequickbrownfoxjumpsoverthelazydog"
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

cm = RemoveNonAlphabet(cm0)
cm.set_alphabet(al.ENGLISH)
plaintext = "I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!"
encdec(cm, plaintext)

cm = Block(cm, length=5, sep="-")
plaintext = "This text is divided by blocks of length 5!"
encdec(cm, plaintext)

'''
Output:

========================================================================================
thequickbrownfoxjumpsoverthelazydog
wkhtxlfneurzqiramxpsvryhuwkhodcbgrj
thequickbrownfoxjumpsoverthelazydog
========================================================================================
schweißgequältvomödentextzürnttypografjakob
vfkzhlcjhtxßowyrpaghqwhäwübuqwwösrjudimdnre
schweißgequältvomödentextzürnttypografjakob
========================================================================================
faqomschweizklövdutrångpjäxby
idtrpvfkzhlönocygxwuaqjsmbåeä
faqomschweizklövdutrångpjäxby
--------------------------------------------------------------------
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
L oryh qrq-doskdehw fkdudfwhuv. Wkhvh duh : ^,&@$~(*;?&#. Wkdw'v lw!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
--------------------------------------------------------------------
Jj becomes Ii because we use ENGLISH_SQUARE_IJ!
Mm ehfrphv Mm ehfdxvh zh xvh HQKOMVL_VTXDUH_MM!
Ii becomes Ii because we use ENGLISH_SQUARE_II!
--------------------------------------------------------------------
text あい だやぎへぐゆぢ
text いう ぢゆぐほげよづ
text あい だやぎへぐゆぢ
--------------------------------------------------------------------
I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!
jepoumpwfopobmqibcfudibsbdufstjxjmmsfnpwfbmmpguifnhsfbu
idontlovenonalphabetcharactersiwillremoveallofthemgreat
--------------------------------------------------------------------
This text is divided by blocks of length 5!
uijtu-fyujt-ejwje-feczc-mpdlt-pgmfo-hui
thistextisdividedbyblocksoflength
'''
