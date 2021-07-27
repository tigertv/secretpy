#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Autokey, CryptMachine, alphabets as al
from secretpy.cmdecorators import UpperCase, Block, SaveAll


alphabet = al.GERMAN
plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = "queenly"

cipher = Autokey()
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

cm = cm0
cm.set_alphabet(al.ENGLISH + al.DECIMAL)
cm.set_key("keys")
plaintext = "I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!"
encdec(cm, plaintext)

cm = Block(cm, length=5, sep="-")
plaintext = "This text is divided by blocks of length 5!"
encdec(cm, plaintext)

cm = SaveAll(cm0)
plaintext = "I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!"
encdec(cm, plaintext)

cm.set_alphabet(al.ENGLISH_SQUARE_IJ)
plaintext = "Jj becomes Ii because we use ENGLISH_SQUARE_IJ!"
encdec(cm, plaintext)

cm.set_alphabet(al.JAPANESE_HIRAGANA)
cm.set_key(u"かぎ")
plaintext = u"text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !"
encdec(cm, plaintext)

cm = UpperCase(cm)
alphabet = al.GREEK
cm.set_alphabet(alphabet)
cm.set_key(u"κλειδί")
plaintext = u"Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)"
encdec(cm, plaintext)

'''
thequickbrownfoxjumpsoverthelazydog
föiudtäßivamvhyyäeeüxüonhbwwzvßlwvk
thequickbrownfoxjumpsoverthelazydog
--------------------------------------------------------------------
I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!
shc51o28xy28ey3uamt0cieacjtvru10z3tdmxzcimz6sf4ssrzyimz
idontlovenonalphabetcharactersiwillremoveallofthemgreat
--------------------------------------------------------------------
This text is divided by blocks of length 5!
3l6ac-l5b1w-0130g-myj1f-op0l3-2hvw1-l4li
thistextisdividedbyblocksoflength5
--------------------------------------------------------------------
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
S pcdm y28-ey3uamt0 cieacjtvru. Clvax hvw : ^,&@$~(*;?&#. Xhrx'b pt!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
--------------------------------------------------------------------
Jj becomes Ii because we use ENGLISH_SQUARE_IJ!
Sn zwlwniu Wu fwlivwg wy mwa IGYPNEO_CYMHIU_CI!
Ii becomes Ii because we use ENGLISH_SQUARE_II!
--------------------------------------------------------------------
text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !
text きうひつけえょ をすらぺだ むぁぽだぷほ すむよたし るゐざきびりよ わじすばぬ えへきありひぁ ゑじぇもあ !
text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !
--------------------------------------------------------------------
Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)
ΣΠΌΝΜ ΊΏΙΈΛ ΤΑΑ ΨΙΣΧΗ Ό ΨΆΌΗΟΚΎΎΕ. (ΥΎΉΘΟΑΣ ΨΕΓΗΟΛ)
ΉΈΛΕΙ ΑΣΕΤΉ ΚΑΘ ΤΌΚΜΗ Ή ΕΛΈΥΘΔΡΊΏ. (ΑΝΕΡΈΆΣ ΚΑΛΒΞΤ)
'''
