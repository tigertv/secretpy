#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot13 

def encdec(cipher, plaintext, alphabet):
	print("----------------------------------")
	print(plaintext)
	enc = cipher.encrypt(plaintext, "", alphabet)
	print(enc)
	dec = cipher.decrypt(enc, "", alphabet)
	print(dec)

alphabet = u"abcdefghijklmnopqrstuvwxyzäöüß"
plaintext  = u"thequickbrownfoxjumpsoverthelazydog"

cipher = Rot13();

encdec(cipher, plaintext, alphabet)

#######################################################

print("----------------------------------")

plaintext  = u"thisisasecretmessage"

print(plaintext)

# use default english alphabet 5x5
enc = cipher.encrypt(plaintext)
print(enc)
dec = cipher.decrypt(enc)
print(dec)

#######################################################

alphabet = u"абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
plaintext  = u"текст"
encdec(cipher, plaintext, alphabet)

