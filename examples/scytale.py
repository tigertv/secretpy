#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Scytale, CryptMachine, alphabets as al
from secretpy.cmdecorators import UpperCase, Block, SaveAll


alphabet = al.GERMAN
plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = 3
cipher = Scytale()

print(plaintext)
enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)


def encdec(machine, plaintext):
    print("--------------------------------------------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))


cm0 = CryptMachine(cipher, key)
cm0.set_alphabet(al.ENGLISH + al.DECIMAL)

cm = cm0
plaintext = "I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!"
encdec(cm, plaintext)

cm = UpperCase(Block(cm, length=5, sep="-"))
plaintext = "This text is divided by blocks of length 5!"
encdec(cm, plaintext)

cm = SaveAll(cm0)
plaintext = "I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!"
encdec(cm, plaintext)

cm.set_alphabet(al.JAPANESE_HIRAGANA)
plaintext = u"text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !"
encdec(cm, plaintext)

cm = UpperCase(cm)
alphabet = al.GREEK
cm.set_alphabet(alphabet)
plaintext = u"Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)"
encdec(cm, plaintext)

'''
thequickbrownfoxjumpsoverthelazydog
tqcrnxmorezohukofjpvtlygeibwousehad
thequickbrownfoxjumpsoverthelazydog
--------------------------------------------------------------------
I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!
inonahehaeilevlfertdtvolatacrwlmeltmeolenpbcrtsiroaohga
idontlovenonalphabetcharactersiwillremoveallofthemgreat
--------------------------------------------------------------------
This text is divided by blocks of length 5!
TSXSV-EYOSL-G5HTT-DIDBC-OETIE-IIDBL-KFNH
THISTEXTISDIVIDEDBYBLOCKSOFLENGTH5
--------------------------------------------------------------------
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
I vola tac-rheeaile npbcrtseat. Ttona heh : ^,&@$~(*;?&#. Aets'r hs!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
--------------------------------------------------------------------
text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !
text いにとぬわたつ らのやふて きみもろほち るかれねむ おゐまこあゆし せはへりを よそなうくけえ ゑさめひす !
text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !
--------------------------------------------------------------------
Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)
ΘΕΡΉΙ ΛΗΕΕΑ ΔΑΆ ΟΈΙΕΚ Τ ΜΕΥΡΑΡΣΛΣ. (ΛΑΤΑΌΗΛ ΘΊΝΈΚΒ)
ΘΈΛΕΙ ΑΡΕΤΉ ΚΑΙ ΤΌΛΜΗ Η ΕΛΕΥΘΕΡΊΑ. (ΑΝΔΡΈΑΣ ΚΆΛΒΟΣ)
'''
