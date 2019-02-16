#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy.keyword import Keyword
import unittest

class TestKeyword(unittest.TestCase):
	alphabet = (u"abcdefghijklmnopqrstuvwxyz",
		u"абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
		u"abcdefghijklmnopqrstuvwxyzäöüß",
		u"abcdefghijklmnñopqrstuvwxyz",
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

	key = (u"kryptos",
		u"криптос",
		u"schlüssel",
		u"clave",
		u"やへぐぢ")

	plaintext = (u"knowledgeispower",
		u"знаниеэтосила",
		u"textnachtricht",
		u"unmensajedetexto",
		u"だやぎへぐゆぢ")

	ciphertext = (u"dghvetpstbmihvtl",
		u"бжкжвоэнзмвек",
		u"rüwrkshbrpdhbr",
		u"tmkemrchevesexsñ",
		u"つもくひけゆて")

	def test_encrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			enc = Keyword().encrypt(self.plaintext[i], self.key[i], alphabet)
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			dec = Keyword().decrypt(self.ciphertext[i], self.key[i], alphabet)
			self.assertEqual(dec, self.plaintext[i])

if __name__ == '__main__': 
	unittest.main()
