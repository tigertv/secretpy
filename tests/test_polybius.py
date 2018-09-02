#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy.polybius import Polybius
import unittest

class TestPolybius(unittest.TestCase):
	alphabet = ([u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"ij", u"k", u"l", u"m", u"n", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z"],
		[u"а",u"б",u"в",u"г",u"д",u"её",u"ж",u"з",u"ий",u"к",u"л",u"м",u"н",u"о",u"п",u"р",u"с",u"т",u"у",u"ф",u"х",u"ц",u"ч",u"ш",u"щ",u"ы",u"ьъ",u"э",u"ю",u"я"],
		[u"aä", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"ij", u"k", u"l", u"m", u"n", u"oö", u"p", u"q", u"r", u"sß", u"t", u"uü", u"v", u"w", u"x", u"y", u"z"],
		[u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"ij", u"k", u"l", u"m", u"nñ", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z"],
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
		)
	)

	key	= (u"key",
		u"ключ",
		u"schlüssel",
		u"clave",
		u"やへぐぢ")

	plaintext  = (u"sometext",
		u"текст",
		u"textnachtricht",
		u"unmensajedetexto",
		u"だやぎへぐゆぢ")

	ciphertext = (u"xtrkykcy",
		u"шмрчш",
		u"ykcysfhnywohny",
		u"zsrksxfokikykcyt",
		u"のをざぷじんは")

	def test_encrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			enc = Polybius().encrypt(alphabet, self.key[i], self.plaintext[i])
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			dec = Polybius().decrypt(alphabet, self.key[i], self.ciphertext[i])

			plaintext = list(self.plaintext[i])
			for i in range(len(plaintext)):
				char = plaintext[i]

				for j in range(len(alphabet)):
					try:
						alphabet[j].index(char)
						break
					except:
						pass
				
				plaintext[i] = list(alphabet[j])[0]
			plaintext = "".join(plaintext)

			self.assertEqual(dec, plaintext)

if __name__ == '__main__': 
	unittest.main()
