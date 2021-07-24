#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Affine, CryptMachine, alphabets as al
from secretpy.cmdecorators import UpperCase, Block, SaveAll


alphabet = al.ENGLISH
plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = (7, 8)

cipher = Affine()
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
cm.set_alphabet(al.ENGLISH)
cm.set_key(key)
plaintext = "I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!"
encdec(cm, plaintext)

cm = Block(cm, length=4, sep="/=/")
cm.set_alphabet(al.SWEDISH + al.DECIMAL)
plaintext = "This text is divided by blocks of length 4!"
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
thequickbrownfoxjumpsoverthelazydog
lfkqsmwapxcgvrcntsojeczkxlfkhibudcy
thequickbrownfoxjumpsoverthelazydog
================================================================================
I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!
mdcvlhczkvcvihjfipklwfixiwlkxemgmhhxkoczkihhcrlfkoyxkil
idontlovenonalphabetcharactersiwillremoveallofthemgreat
================================================================================
This text is divided by blocks of length 4!
yszr/=/y7ny/=/zr0z/=/9z07/=/0pup/=/höwa/=/röeh/=/7vly/=/sf
thistextisdividedbyblocksoflength4
================================================================================
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
Z hö97 vöv-ih6sip7y wsikiwy7kr. Ys7r7 ik7 : ^,&@$~(*;?&#. Ysiy'r zy!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
================================================================================
Jj becomes Ii because we use ENGLISH_SQUARE_IJ!
Pp qmxzlmc Pp qmxircm fm rcm MSADPCH_CORIVM_PP!
Ii becomes Ii because we use ENGLISH_SQUARE_II!
================================================================================
text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !
text さじやづぐかも ねあのくな てへよぢごる ばびたをつ ずゐぺにむべげ りぁゃとぷ けぬぱまどざほ ゑろひめぴ !
text いろはにほへと ちりぬるを わかよたれそ つねならむ うゐのおくやま けふこえて あさきゆめみし ゑひもせす !
================================================================================
Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)
ΛΟΘΙΡ ΗΦΙΝΖ ΓΗΡ ΝΚΘΞΑ Α ΙΘΙΣΛΙΦΧΗ. (ΗΤΔΦΟΗΉ ΓΜΘΣΈΉ)
ΘΈΛΕΙ ΑΡΕΤΉ ΚΑΙ ΤΌΛΜΗ Η ΕΛΕΒΘΕΡΊΑ. (ΑΝΔΡΈΑΣ ΚΆΛΒΟΣ)
'''
