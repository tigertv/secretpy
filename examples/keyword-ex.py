#!/usr/bin/python
# -*- encoding: utf-8 -*-
from secretpy import Keyword, CryptMachine, alphabets as al
from secretpy.cmdecorators import UpperCase, Block, SaveAll


alphabet = al.GERMAN
plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = "queenly"

cipher = Keyword()
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
cm.set_alphabet(al.DECIMAL + al.ENGLISH)
cm.set_key("manykeys")
plaintext = "I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!"
encdec(cm, plaintext)

cm = UpperCase(Block(cm, length=5, sep="-"))
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
rblmscefuojviyjwdshkpjtlorblgqzxnja
thequickbrownfoxjumpsoverthelazydog
--------------------------------------------------------------------
I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!
c6jirgju7iji3glb347r5b3p35r7pqcvcggp7hju73ggj8rb7h9p73r
idontlovenonalphabetcharactersiwillremoveallofthemgreat
--------------------------------------------------------------------
This text is divided by blocks of length 5!
RBCQR-7WRCQ-6CUC6-764X4-GJ5FQ-J8G7I-9RBE
THISTEXTISDIVIDEDBYBLOCKSOFLENGTH5
--------------------------------------------------------------------
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
C gju7 iji-3glb347r 5b3p35r7pq. Rb7q7 3p7 : ^,&@$~(*;?&#. Rb3r'q cr!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
--------------------------------------------------------------------
Jj becomes Ii because we use ENGLISH_SQUARE_IJ!
Cc aknigkq Cc aknmtqk vk tqk KHSFCQB_QOTMPK_CC!
Ii becomes Ii because we use ENGLISH_SQUARE_II!
--------------------------------------------------------------------
text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !
text ぎろはにほへと ちりぬるを わえよたれそ つねならむ あゐのうきやま くふけいて かさおゆめみし ゑひもせす !
text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !
--------------------------------------------------------------------
Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)
ΈΑΘΊΖ ΚΡΊΤΓ ΉΚΖ ΤΌΘΜΒ Β ΊΘΊΥΈΊΡΗΚ. (ΚΝΔΡΑΚΣ ΉΛΘΕΟΣ)
ΘΈΛΕΙ ΑΡΕΤΉ ΚΑΙ ΤΌΛΜΗ Η ΕΛΕΥΘΕΡΊΑ. (ΑΝΔΡΈΑΣ ΚΆΛΒΟΣ)
'''
