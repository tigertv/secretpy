#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import MyszkowskiTransposition, CryptMachine, alphabets as al
from secretpy.cmdecorators import UpperCase, Block, SaveAll

alphabet = al.GERMAN
plaintext = u"schweißgequältvomödentextzürnttypografjakob"
key = u"schlüssel"

cipher = MyszkowskiTransposition()
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
cm.set_alphabet(al.ENGLISH)
cm.set_key("tomatokey")
plaintext = "I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!"
encdec(cm, plaintext)

cm = Block(cm, length=5, sep="-")
plaintext = "This text is divided by blocks of length 5!"
encdec(cm, plaintext)

cm = SaveAll(cm0)
plaintext = "I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!"
encdec(cm, plaintext)

cm.set_alphabet(al.JAPANESE_HIRAGANA)
cm.set_key(u"かぎはにかぎ")
plaintext = u"text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !"
encdec(cm, plaintext)

cm = UpperCase(cm)
alphabet = al.GREEK
cm.set_alphabet(alphabet)
cm.set_key(u"κλειδί")
plaintext = u"Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)"
encdec(cm, plaintext)

cm.set_key(u"kryptonyckeln")
cm.set_alphabet(al.SWEDISH)
plaintext = u"FAQ om Schweiz: Klöv du trång pjäxby?"
encdec(cm, plaintext)

'''
schweißgequältvomödentextzürnttypografjakob
cuenfgmzghäntjwelötütrasißqvodxtrpoaobeteyk
schweißgequältvomödentextzürnttypografjakob
--------------------------------------------------------------------
I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!
nahivevaclleohallroncsohdloptrrimatgitnleaeweefmtebtroa
idontlovenonalphabetcharactersiwillremoveallofthemgreat
--------------------------------------------------------------------
This text is divided by blocks of length 5!
svogt-doxes-iilnh-eddbk-ehtts-iyclt-ibf
thistextisdividedbyblocksoflength
--------------------------------------------------------------------
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
V acei ncs-totreoha sslnpereer. Tielb ath : ^,&@$~(*;?&#. Aata'h th!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
--------------------------------------------------------------------
text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !
text いほとるわれつ むのまふあ きしもろへち をかそねう おゐけこさゆひ せにぬたら やてみはりよな ゑくえめす !
text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !
--------------------------------------------------------------------
Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)
ΙΚΜΥΑ ΣΣΛΤΌ ΛΊΈ ΒΕΉΛΕ Α ΑΟΑΑΗΘΝΚΘ. (ΡΙΗΕΔΆΈ ΕΤΕΡΡΛ)
ΘΈΛΕΙ ΑΡΕΤΉ ΚΑΙ ΤΌΛΜΗ Η ΕΛΕΥΘΕΡΊΑ. (ΑΝΔΡΈΑΣ ΚΆΛΒΟΣ)
--------------------------------------------------------------------
FAQ om Schweiz: Klöv du trång pjäxby?
WNI PF ELGXZJC: KRÄS TO DAÖBM UQHVÅY?
FAQ OM SCHWEIZ: KLÖV DU TRÅNG PJÄXBY?
'''
