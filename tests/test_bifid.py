#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy.bifid import Bifid
from unittest import TestCase

class TestBifid(TestCase):
	alphabet = (
		[
			u"b", u"g", u"w", u"k", u"z",
			u"q", u"p", u"n", u"d", u"s", 
			u"ij", u"o", u"a", u"x", u"e", 
			u"f", u"c", u"l", u"u", u"m", 
			u"t", u"h", u"y", u"v", u"r"
		],
		[
			u"p", u"h", u"q", u"g", u"m",
			u"e", u"a", u"y", u"l", u"n", 
			u"o", u"f", u"d", u"x", u"k", 
			u"r", u"c", u"v", u"s", u"z", 
			u"w", u"b", u"u", u"t", u"ij"
		],
		[
			u"aä", u"b", u"c", u"d", u"e", 
			u"f", u"g", u"h", u"ij", u"k", 
			u"l", u"m", u"n", u"oö", u"p", 
			u"q", u"r", u"sß", u"t", u"uü", 
			u"v", u"w", u"x", u"y", u"z"
		],
		[
			u"a", u"b", u"c", u"d", u"e", 
			u"f", u"g", u"h", u"ij", u"k", 
			u"l", u"m", u"nñ", u"o", u"p", 
			u"q", u"r", u"s", u"t", u"u", 
			u"v", u"w", u"x", u"y", u"z"
		],
		[
			u"а", u"б", u"в", u"г", u"д",u"её",
			u"ж", u"з", u"ий", u"к", u"л", u"м", 
			u"н", u"о", u"п", u"р", u"с", u"т",
			u"у", u"ф", u"х", u"ц", u"ч", u"ш", 
			u"щ", u"ы", u"ьъ", u"э", u"ю", u"я",
			u"1", u"2", u"3", u"4", u"5", u"6",
		],
		(
			u"あいうえお"
			u"かきくけこ"
			u"がぎぐげご"
			u"さしすせそ"
			u"ざじずぜぞ"
			u"たちつてと"
			u"だぢづでど"
			u"なにぬねの"
			u"はひふへほ"
			u"ばびぶべぼ"
			u"ぱぴぷぺぽ"
			u"まみむめも"
			u"やゆよ"
			u"らりるれろ"
			u"わを"
			u"ん"
			u"ゃゅょぁぇ"
			u"じづ"
		),
	
	)

	'''
		'''

	key	= (
		0,
		5,
		7,
		4,
		4,
		6,
	)

	plaintext  = (
		u"fleeatonce",
		u"defendtheeastwallofthecastle",
		u"textnachtricht",
		u"unmensaiedetexto",
		u"текст",
		u"だやぎへぐゆぢ",
	)

	ciphertext = (
		u"uaeolwrins",
		u"ffyhmkhycpliashadtrlhcchlblr",
		u"qyldxscirbsrso",
		u"slxkobndadyyesxt",
		u"ни6чт",
		u"でげさでたどぢ",
	)

	def setUp(self):
		self.cipher = Bifid()

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
