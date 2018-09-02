#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy.vigener import Vigener 
import unittest

class TestVigener(unittest.TestCase):
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

	key = (u"lemon",
		u"ключ",
		u"schlüssel",
		u"clave",
		u"やへぐぢ")

	plaintext  = (u"attackatdawn",
		u"текст",
		u"textnachtricht",
		u"unmensajedetexto",
		u"だやぎへぐゆぢ")

	ciphertext = (u"lxfopvefrnhr",
		u"эрииэ",
		u"hgaalsulafkjsr",
		u"wxmzquljzhgeesxq",
		u"ぐたぜぁゅちへ")

	def test_encrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			enc = Vigener().encrypt(alphabet, self.key[i], self.plaintext[i])
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			dec = Vigener().decrypt(alphabet, self.key[i], self.ciphertext[i])
			self.assertEqual(dec, self.plaintext[i])

if __name__ == '__main__': 
	unittest.main()
