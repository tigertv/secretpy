#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import ColumnarTransposition, CryptMachine, alphabets as al
from secretpy.cmdecorators import SaveAll, Block


cipher = ColumnarTransposition()
key = "cargo"
plaintext = "attackatdawn"

print(plaintext)
enc = cipher.encrypt(plaintext, key)
print(enc)
print(cipher.decrypt(enc, key))
print('========================================================================================')


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))
    print("-----------------------------------------------------------")


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

'''
attackatdawn
tanakwadcatt
attackatdawn
========================================================================================
I don't love non-alphabet characters and uppercase. I will remove all of them: ^,&@$~(*;?&#.
donahtneelvomilohccapslolenelerrucweattnptaspaimlhovabaedriref
idontlovenonalphabetcharactersanduppercaseiwillremoveallofthem
-----------------------------------------------------------
This text is divided by blocks of length 5!
hxido ftted elogs iiyke tsdbs nitvb clh
thistextisdividedbyblocksoflength
-----------------------------------------------------------
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
L ohcc taa-inptaseh tvabaeeese. Lerrs tio : ^,&@$~(*;?&#. Naht'h rt!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
-----------------------------------------------------------
text あい だやぎへぐゆぢ
text だぐ あぎぢやゆいへ
text あい だやぎへぐゆぢ
-----------------------------------------------------------
'''
