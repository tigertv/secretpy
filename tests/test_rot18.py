#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot18
from unittest import TestCase
from secretpy import alphabet

class TestRot18(TestCase):

	plaintext  = (
		u"agirlhas12345cats",
		u"удевочки12345кошек",
		u"einmädchenhat12345katze",
		u"unaniñatiene12345gatos",
	)

	ciphertext = (
		u"ntveyunf67890pngf",
		u"гфхтяжыщ67890ыязхы",
		u"txüölsrwtüwpe67890zpekt",
		u"hnñnvañgvrnr67890tñgbf",
	)

	alphabets = (
		alphabet.ENGLISH,
		alphabet.RUSSIAN,
		alphabet.GERMAN,
		alphabet.SPANISH,
	)

	def setUp(self):
		self.cipher = Rot18()

	def test_encrypt(self):
		for i,plaintext in enumerate(self.plaintext):
			enc = self.cipher.encrypt(plaintext, alphabet=self.alphabets[i])
			print(enc)
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		for i,plaintext in enumerate(self.plaintext):
			dec = self.cipher.decrypt(self.ciphertext[i], alphabet=self.alphabets[i])
			self.assertEqual(dec, plaintext)

if __name__ == '__main__': 
	unittest.main()
