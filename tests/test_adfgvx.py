#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy.adfgvx import ADFGVX
import unittest

class TestADFGVX(unittest.TestCase):
	alphabet = (
		[
			u"b", u"t", u"a", u"l", u"p", u"5",
			u"d", u"h", u"o", u"z", u"k", u"4",
			u"q", u"f", u"v", u"s", u"n", u"3",
			u"g", u"ij", u"c", u"u", u"x", u"2",
			u"m", u"r", u"e", u"w", u"y", u"1",
			u".", u"0", u"9", u"8", u"7", u"6",
		],
		[
			u"aä", u"b", u"c", u"d", u"e", u"9",
			u"f", u"g", u"h", u"ij", u"k", u"7",
			u"l", u"m", u"n", u"oö", u"p",  u"8",
			u"q", u"r", u"sß", u"t", u"uü",  u"5",
			u"v", u"w", u"x", u"y", u"z", u"0",
			u"1", u"3", u"2", u"4", u"6", u".",
		],
		[
			u"a", u"b", u"c", u"d", u"e", u"5",
			u"f", u"g", u"h", u"ij", u"k", u"4",
			u"l", u"m", u"nñ", u"o", u"p", u"3",
			u"q", u"r", u"s", u"t", u"u", u"2",
			u"v", u"w", u"x", u"y", u"z", u"1",
			u".", u"9", u"7", u"6", u"8", u"0",
		],
	)

	key	= (
		u"cargo",
		u"schlüssel",
		u"clave",
	)

	plaintext  = (
		u"attackatonce",
		u"textnachtricht",
		u"unmensaiedetexto",
	)

	ciphertext = (
		u"favdfadddgdgfffafavafafv",
		u"gadggfaadvagfgggfggfdfgfdvfa",
		u"fvavgfgdggavfffdgagvafavvgffaagg",
	)

	chipher = ADFGVX() 

	def test_encrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			enc = self.chipher.encrypt(self.plaintext[i], self.key[i], alphabet)
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			dec = self.chipher.decrypt(self.ciphertext[i], self.key[i], alphabet)
			self.assertEqual(dec, self.plaintext[i])

if __name__ == '__main__': 
	unittest.main()
