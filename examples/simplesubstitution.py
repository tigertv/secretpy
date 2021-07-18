#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import SimpleSubstitution, CryptMachine, alphabets as al
from secretpy.cmdecorators import Block, SaveAll


cipher = SimpleSubstitution()
alphabet = al.GERMAN
plaintext = u"schweißgequältvomödentextzürnttypografjakob"
key = u"fwxyäöeßüdabcglmnpqrstuvhjoikz"

print(plaintext)
enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)

#######################################################


def encdec(machine, plaintext):
    print("--------------------------------------------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))


cm0 = CryptMachine(cipher, key)

cm = cm0
cm.set_alphabet(al.ENGLISH)
cm.set_key("yzabchijkdeflmntuvwxopqrsg")
plaintext = "I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!"
encdec(cm, plaintext)

cm = Block(cm, length=5, sep=")(")
plaintext = "This text is divided by blocks of length 5!"
encdec(cm, plaintext)

cm = SaveAll(cm0)
plaintext = "I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!"
encdec(cm, plaintext)

cm.set_alphabet(al.ENGLISH_SQUARE_IJ)
key = (
    "n", "g", "a", "b", "l",
    "s", "t", "u", "v", "c",
    "m", "o", "p", "q", "h",
    "ij", "k", "w", "x", "y",
    "r", "d", "e", "f", "z"
)
cm.set_key(key)
plaintext = "Jj becomes Ii because we use ENGLISH_SQUARE_IJ!"
encdec(cm, plaintext)

alphabet = u"abcdABCDEfghijFGHIJ"
key = u"dABDFIJEfgCHabchijG"
cm.set_alphabet(alphabet)
cm.set_key(key)
plaintext = u"Text aBcdHijf"
encdec(cm, plaintext)

'''
schweißgequältvomödentextzürnttypografjakob
qxßuäüzeänsobrtlciyägrävrjkpgrrhmlepfödfalw
schweißgequältvomödentextzürnttypografjakob
--------------------------------------------------------------------
I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!
kbnmxfnpcmnmyftjyzcxajyvyaxcvwkqkffvclnpcyffnhxjclivcyx
idontlovenonalphabetcharactersiwillremoveallofthemgreat
--------------------------------------------------------------------
This text is divided by blocks of length 5!
xjkwx-crxkw-bkpkb-cbzsz-fnaew-nhfcm-ixj
thistextisdividedbyblocksoflength
--------------------------------------------------------------------
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
K fnpc mnm-yftjyzcx ajyvyaxcvw. Xjcwc yvc : ^,&@$~(*;?&#. Xjyx'w kx!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
--------------------------------------------------------------------
Jj becomes Ii because we use ENGLISH_SQUARE_IJ!
Vv glaqolw Vv glanywl dl ywl LPTMVWU_WIYNKL_VV!
Ii becomes Ii because we use ENGLISH_SQUARE_II!
--------------------------------------------------------------------
Text aBcdHijf
Text dIBDiabg
Text aBcdHijf
'''
