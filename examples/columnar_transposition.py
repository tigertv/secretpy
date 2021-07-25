#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import ColumnarTransposition, CryptMachine, alphabets as al
from secretpy.cmdecorators import SaveAll, Block


cipher = ColumnarTransposition()
alphabet = al.GERMAN
plaintext = u"schweißgequältvomödentextzürnttypografjakob"
key = u"schlüssel"

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


key = "manykeys"
cm0 = CryptMachine(cipher, key)

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

cm.set_alphabet(al.JAPANESE_HIRAGANA)
cm.set_key(u"だやぎへ")
plaintext = u"text あい だやぎへぐゆぢ"
encdec(cm, plaintext)

cm.set_alphabet(al.ENGLISH_SQUARE_IJ)
cm.set_key(u"keyj")
plaintext = "ENGLISH_SQUARE_IJ doesn't change Ii to Jj because it's a transposition cipher!"
encdec(cm, plaintext)

'''
schweißgequältvomödentextzürnttypografjakob
cuenfgmzghäntjwlttaeöürsqdraivxpoßotobeteyk
schweißgequältvomödentextzürnttypografjakob
================================================================================
I don't love non-alphabet characters and uppercase. I will remove all of them: ^,&@$~(*;?&#.
dnbcuemfllhsrlamtacreieeieaadseoooetpiotvhrnarlnntepwvhopaacll
idontlovenonalphabetcharactersanduppercaseiwillremoveallofthem
================================================================================
This text is divided by blocks of length 5!
hsboe iontv letid shidy ftekt siblx dcg
thistextisdividedbyblocksoflength
================================================================================
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
L lhse nbc-steaaeai acrrtopatt. Nteai vhr : ^,&@$~(*;?&#. Hhoe't es!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
================================================================================
text あい だやぎへぐゆぢ
text だぐ あぎぢやゆいへ
text あい だやぎへぐゆぢ
================================================================================
ENGLISH_SQUARE_IJ doesn't change Ii to Jj because it's a transposition cipher!
NSUIECG_TBUTRP_TC elsrd'n aijcea Ns op Ei qeotnij ai't s inhghajsheoes saoiir!
ENGLISH_SQUARE_IJ doesn't change Ii to Jj because it's a transposition cipher!
'''
