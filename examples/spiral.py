#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Spiral, CryptMachine, alphabets as al
from secretpy.cmdecorators import SaveAll, Block, UpperCase


cipher = Spiral()
key = 5
alphabet = al.GERMAN
plaintext = u"schweißgequältvomödentextzürnttypografjakob"

print(plaintext)
enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)


def encdec(machine, plaintext):
    print("=" * 80)
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))


cm0 = CryptMachine(cipher, key)

cm = cm0
cm = UpperCase(Block(cm0))
key = 5
cm.set_key(key)
cm.set_alphabet(al.ENGLISH)
plaintext = "WE ARE DISCOVERED FLEE AT ONCE"
encdec(cm, plaintext)

cm = cm0
cm.set_alphabet(al.ENGLISH)
plaintext = "I don't love non-alphabet characters and uppercase. I will remove all of them: ^,&@$~(*;?&#."
encdec(cm, plaintext)

cm = Block(cm, length=5, sep=" ")
plaintext = "This text is divided by blocks of length 5!"
encdec(cm, plaintext)

cm = SaveAll(cm0)
plaintext = "I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!"
encdec(cm, plaintext)

cm.set_alphabet(al.ENGLISH_SQUARE_IJ)
plaintext = "ENGLISH_SQUARE_IJ doesn't change Ii to Jj because it's a transposition cipher!"
encdec(cm, plaintext)

cm.set_alphabet(al.JAPANESE_HIRAGANA)
cm.set_key(4)
plaintext = u"text あい だやぎへぐゆぢ"
encdec(cm, plaintext)


'''
schweißgequältvomödentextzürnttypografjakob
kobagttevqewhcsiuonztrafjonxdtegßämtüypreöl
schweißgequältvomödentextzürnttypografjakob
================================================================================
WE ARE DISCOVERED FLEE AT ONCE
TONCE ADOER AEWDV FLEEE CSIER
WEAREDISCOVEREDFLEEATONCE
================================================================================
I don't love non-alphabet characters and uppercase. I will remove all of them: ^,&@$~(*;?&#.
emhlmiapsatpntnodilohccapsloloftaewcurrelevonahtneelverirdeaba
idontlovenonalphabetcharactersanduppercaseiwillremoveallofthem
================================================================================
This text is divided by blocks of length 5!
gthns bdsts ihted elofl ekyii txido cbv
thistextisdividedbyblocksoflength
================================================================================
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
T itsr rel-evolinpt asehatseee. Abano hcc : ^,&@$~(*;?&#. Tarh't ha!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
================================================================================
ENGLISH_SQUARE_IJ doesn't change Ii to Jj because it's a transposition cipher!
HERPIPT_EETNNJ_UI lgnes'a dtgoci Ro on Ci tsasbia si'q s hrocejatasins ujihee!
ENGLISH_SQUARE_IJ doesn't change Ii to Jj because it's a transposition cipher!
================================================================================
text あい だやぎへぐゆぢ
text ぢゆ やだいあぎへぐ
text あい だやぎへぐゆぢ
'''
