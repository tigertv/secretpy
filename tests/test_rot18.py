#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot18
from unittest import TestCase

class TestRot18(TestCase):

	plaintext  = (
		u"agirlhas12345cats",
	)

	ciphertext = (
		u"ntveyunf67890pngf",
	)

	cipher = Rot18()

	def test_encrypt(self):
		for i,plaintext in enumerate(self.plaintext):
			enc = self.cipher.encrypt(plaintext)
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		for i,plaintext in enumerate(self.plaintext):
			dec = self.cipher.decrypt(self.ciphertext[i])
			self.assertEqual(dec, plaintext)

if __name__ == '__main__': 
	unittest.main()
