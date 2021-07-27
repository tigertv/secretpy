#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Gronsfeld, CryptMachine, alphabets as al
from secretpy.cmdecorators import UpperCase, Block, SaveAll


alphabet = al.GERMAN
plaintext = u"schweißgequältvomödentextzürnttypografjakob"
key = (4, 17, 9)

cipher = Gronsfeld()

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


key = (14, 2, 11)
cm0 = CryptMachine(cipher, key)

cm = cm0
cm.set_alphabet(al.ENGLISH)
plaintext = "I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!"
encdec(cm, plaintext)

cm = Block(cm, length=5, sep=" ")
cm.set_key((1, 12, 7, 2))
plaintext = "This text is divided by blocks of length 5!"
encdec(cm, plaintext)

cm = SaveAll(cm0)
plaintext = "I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!"
encdec(cm, plaintext)

cm.set_alphabet(al.ENGLISH_SQUARE_IJ)
plaintext = "Jj becomes Ii because we use ENGLISH_SQUARE_IJ!"
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
schweißgequältvomödentextzürnttypografjakob
wtqävrdxnuhfpgasßghvwxvcxmhvaüxlysxäewseöxf
schweißgequältvomödentextzürnttypografjakob
--------------------------------------------------------------------
I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!
wfzbvwcxpbqyonavcmsvnvccoeestdwytzncsozjglznztvssorfglh
idontlovenonalphabetcharactersiwillremoveallofthemgreat
--------------------------------------------------------------------
This text is divided by blocks of length 5!
utpuu qevje kkwuk genfd majmt amnfz nvi
thistextisdividedbyblocksoflength
--------------------------------------------------------------------
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
J xvxf zvp-bxwjbnlv dthtboagse. Ajfel csq : ^,&@$~(*;?&#. Ajbf'z ku!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
--------------------------------------------------------------------
Jj becomes Ii because we use ENGLISH_SQUARE_IJ!
Kv igdatgt Vq dfphwtr dg vem GOTSLTU_ZSVNYG_KV!
Ii becomes Ii because we use ENGLISH_SQUARE_II!
--------------------------------------------------------------------
text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !
text うえぶねばまに てるぼゅゃ をすをつろぢ どはにぇり おゐはしごよみ ざぼぎおは くすくょるめす ゑぺれざせ !
text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !
--------------------------------------------------------------------
Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)
ΙΟΡΖΊ ΊΧΖΥΡ ΠΒΊ ΔΎΝΝΠ Μ ΖΜΞΑΊΈΆΌΒ. (ΆΧΙΣΖΊΩ ΜΒΎΉΠΤ)
ΘΈΛΕΙ ΑΡΕΤΉ ΚΑΙ ΤΌΛΜΗ Η ΕΛΕΥΘΕΡΊΑ. (ΑΝΔΠΈΑΣ ΚΆΛΒΟΣ)
'''
