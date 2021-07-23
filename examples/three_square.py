#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import ThreeSquare, CryptMachine, alphabets as al
from secretpy.cmdecorators import UpperCase, SaveAll, Block


def encdec(machine, plaintext):
    print("=" * 80)
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)


key = (u"example", u"keyword", u"third")
cm = UpperCase(CryptMachine(ThreeSquare()))
cm.set_alphabet(al.ENGLISH_SQUARE_OQ)
cm.set_key(key)
plaintext = u"The quick brown fox jumps over the lazy dog!"
encdec(cm, plaintext)

cm = SaveAll(cm)
encdec(cm, plaintext)

cm = SaveAll(CryptMachine(ThreeSquare()))
cm.set_alphabet(al.ENGLISH_SQUARE_IJ)
key = (u"criptog", u"segurt", u"mars")
cm.set_key(key)
plaintext = u"Attack at dawns!!!"
encdec(cm, plaintext)

cm.set_alphabet(al.GREEK_SQUARE)
key = (u"ίκλειδ", u"κλειδί", u"λειδίκ")
cm.set_key(key)
plaintext = u"Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)"
encdec(cm, plaintext)

cm = UpperCase(Block(CryptMachine(ThreeSquare())))
cm.set_alphabet(al.GREEK_SQUARE)
key = (u"ίκλειδ", u"κλειδί", u"λειδίκ")
cm.set_key(key)
encdec(cm, plaintext)

'''
================================================================================
The quick brown fox jumps over the lazy dog!
TPGEDELYICAWBACHSYNNJOSUJJTYRPSUWHWYINTBJELCBTXYSFONMV
THEOUICKBROWNFOXJUMPSOVERTHELAZYDOGZ
================================================================================
The quick brown fox jumps over the lazy dog!
TPJ LDONY IAAEX ARB SOUNH OSXS JVM RMMU EHW!OWNZBJEGCAKXKSFYUMU
THE OUICK BROWN FOX JUMPS OVER THE LAZY DOG!Z
================================================================================
Attack at dawns!!!
Actuac vs ihctz!!!ddnwosuz
Attack at dawns!!!z
================================================================================
Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)
Ινιχι ιιλβρ σετ τβκλβ θ κσωμεμογο. (Γκνιιπυ Οζεσθλ)ζπγξδεσξληςπλαβιβηνετψ
Θελει αρετη και τολμη η ελευθερια. (Ανδρεας Καλβος)ω
================================================================================
Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)
ΠΝΚΛΙ ΕΙΛΒΒ ΣΙΗΤΓ ΜΛΓΑΚ ΣΔΜΕΚ ΟΗΩΓΙ ΣΙΚΠΥ ΜΖΕΠΥ ΛΒΠΓΘ ΤΕΡΞΛ ΖΕΠΕΘ ΒΚΚΗΞ ΞΤΨ
ΘΕΛΕΙΑΡΕΤΗΚΑΙΤΟΛΜΗΗΕΛΕΥΘΕΡΙΑΑΝΔΡΕΑΣΚΑΛΒΟΣΩ
'''
