#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Bazeries, CryptMachine, alphabets as al
from secretpy.cmdecorators import UpperCase, SaveAll


def encdec(machine, plaintext):
    print("=" * 80)
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)


cm = UpperCase(CryptMachine(Bazeries()))
cm.set_alphabet(al.ENGLISH_SQUARE_IJ)

key = (81257, u"eightyonethousandtwohundredfiftyseven")
cm.set_key(key)
plaintext = u"Whoever has made a voyage up the Hudson" \
            u" must remember the Kaatskill mountains"
encdec(cm, plaintext)

cm = SaveAll(cm)
encdec(cm, plaintext)

cm = UpperCase(SaveAll(CryptMachine(Bazeries(), key)))
cm.set_alphabet(al.ENGLISH_SQUARE_IJ)
plaintext = u"The quick brown fox jumps over the lazy dog!"
encdec(cm, plaintext)

cm.set_alphabet(al.GREEK_SQUARE)
cm.set_key((2358, u"κλειδί"))
plaintext = u"Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)"
encdec(cm, plaintext)

'''
================================================================================
Whoever has made a voyage up the Hudson must remember the Kaatskill mountains
DUMTMCDSENRTEMVEQXMOELCCRVXDMDKWXNNMUKRDKUMYNMBPRKEEPMGNGEKWXCRWB
WHOEVERHASMADEAVOYAGEUPTHEHUDSONMUSTREMEMBERTHEKAATSKILLMOUNTAINS
================================================================================
Whoever has made a voyage up the Hudson must remember the Kaatskill mountains
DUMTMCD SEN RTEM V EQXMOE LC CRV XDMDKW XNNM UKRDKUMY NMB PRKEEPMGN GEKWXCRWB
WHOEVER HAS MADE A VOYAGE UP THE HUDSON MUST REMEMBER THE KAATSKILL MOUNTAINS
================================================================================
The quick brown fox jumps over the lazy dog!
PAB XHMDK YCUFC IWS TCRQN XBZE GMD KUML CVO!
THE QUICK BROWN FOX IUMPS OVER THE LAZY DOG!
================================================================================
Θέλει αρετή και τόλμη η ελευθερία. (Ανδρέας Κάλβος)
ΥΜΡΥΕ ΒΨΥΖΚ ΒΓΕ ΧΨΡΚΦ Υ ΒΔΥΕΚΡΖΥΜ. (ΦΣΚΥΖΠΝ ΚΕΚΣΧΑ)
ΘΕΛΕΙ ΑΡΕΤΗ ΚΑΙ ΤΟΛΜΗ Η ΕΛΕΥΘΕΡΙΑ. (ΑΝΔΡΕΑΞ ΚΑΛΒΟΞ)
'''
