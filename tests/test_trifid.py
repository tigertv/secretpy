#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy.trifid import Trifid
from unittest import TestCase

class TestTrifid(TestCase):
	alphabet = (
		[
			u"e", u"p", u"s", 
			u"d", u"u", u"c", 
			u"v", u"w", u"y",

			u"m", u".", u"z", 
			u"l", u"k", u"x", 
			u"n", u"b", u"t", 

			u"f", u"g", u"o", 
			u"r", u"i", u"j", 
			u"h", u"a", u"q",
		],
		[
			u"aä", u"b", u"c", 
			u"d", u"e", u"f", 
			u"g", u"h", u"i", 

			u"j", u"k", u"l", 
			u"m", u"n", u"oö", 
			u"p", u"q", u"r", 

			u"sß", u"t", u"uü", 
			u"v", u"w", u"x", 
			u"y", u"z", u".",
		],
		[
			u"a", u"b", u"c", 
			u"d", u"e", u"f", 
			u"g", u"h", u"i",

			u"j", u"k", u"l",
			u"m", u"nñ", u"o", 
			u"p", u"q", u"r", 

			u"s", u"t", u"u", 
			u"v", u"w", u"x", 
			u"y", u"z", u".",
		],
	
	)

	key	= (
		5,
		7,
		4,
	)

	plaintext  = (
		u"defendtheeastwallofthecastle.",
		u"textnachtricht",
		u"unmensaiedetexto",
	)

	ciphertext = (
		u"suefecphsegyyjiximfofocejlbsp",
		u"uvbkbqlhayytrw",
		u"wbokpdhcawkeinex",
	)

	def setUp(self):
		self.cipher = Trifid()

	def test_encrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			enc = self.cipher.encrypt(self.plaintext[i], self.key[i], alphabet)
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			dec = self.cipher.decrypt(self.ciphertext[i], self.key[i], alphabet)
			self.assertEqual(dec, self.plaintext[i])

if __name__ == '__main__': 
	unittest.main()
