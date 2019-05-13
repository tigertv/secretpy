#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import SimpleSubstitution
from secretpy import alphabets

alphabet = alphabets.GERMAN
plaintext = u"thequickbrownfoxjumpsoverthelazydog"
key = u"dabcghijokzlmnpqrstuvfwxyäöeüß"

cipher = SimpleSubstitution()
print(plaintext)

enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)

#######################################################

print("----------------------------------")

plaintext = u"thisisasecretmessage"
alphabet = alphabets.ENGLISH
key = u"dabcghijokzlmnpqrstuvfwxye"

print(plaintext)
enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
dec = cipher.decrypt(enc, key, alphabet)
print(dec)

'''
thequickbrownfoxjumpsoverthelazydog
ujgrvobzaspwnhpxkvmqtpfgsujgldäycpi
thequickbrownfoxjumpsoverthelazydog
----------------------------------
thisisasecretmessage
ujototdtgbsgumgttdig
thisisasecretmessage
'''
