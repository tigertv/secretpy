#!/usr/bin/python
# -*- encoding: utf-8 -*-

#from secretpy.polybius import Polybius
from secretpy.adfgx import ADFGX
import unittest

class TestADFGX(unittest.TestCase):
	alphabet = (
		[u"b", u"t", u"a", u"l", u"p", u"d", u"h", u"o", u"z", u"k", u"q", u"f", u"v", u"s", u"n", u"g", u"ij", u"c", u"u", u"x", u"m", u"r", u"e", u"w", u"y"],
		#[u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"ij", u"k", u"l", u"m", u"n", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z"],
		#[u"а",u"б",u"в",u"г",u"д",u"её",u"ж",u"з",u"ий",u"к",u"л",u"м",u"н",u"о",u"п",u"р",u"с",u"т",u"у",u"ф",u"х",u"ц",u"ч",u"ш",u"щ",u"ы",u"ьъ",u"э",u"ю",u"я"],
		[u"aä", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"ij", u"k", u"l", u"m", u"n", u"oö", u"p", u"q", u"r", u"sß", u"t", u"uü", u"v", u"w", u"x", u"y", u"z"],
		[u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"ij", u"k", u"l", u"m", u"nñ", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z"],
	)

	key	= (
		u"cargo",
		#u"ключ",
		u"schlüssel",
		u"clave",
	)

	plaintext  = (
		u"attackatonce",
		#u"текст",
		u"textnachtricht",
		u"unmensaiedetexto",
	)

	ciphertext = (
		u"faxdfadddgdgfffafaxafafx",
		#u"dgxffaaaaa",
		u"gadggfaadxagfgggfggfdfgfdxfa",
		u"fxaxgfgdggaxfffdgagxafaxxgffaagg",
	)

	def test_encrypt(self):
		chipher = ADFGX() 
		for i,alphabet in enumerate(self.alphabet):
			enc = chipher.encrypt(self.key[i], self.plaintext[i], alphabet)
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		chipher = ADFGX() 
		for i,alphabet in enumerate(self.alphabet):
			dec = chipher.decrypt(self.key[i], self.ciphertext[i], alphabet)
			self.assertEqual(dec, self.plaintext[i])

if __name__ == '__main__': 
	unittest.main()
