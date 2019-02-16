#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy.beaufort import Beaufort 
import unittest

class TestBeaufort(unittest.TestCase):
	alphabet = (u"abcdefghijklmnopqrstuvwxyz",
		u"abcdefghijklmnopqrstuvwxyzäöüß",
		u"abcdefghijklmnñopqrstuvwxyz",
		u"абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
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

	key = (u"key",
		u"schlüssel",
		u"clave",
		u"ключ",
		u"やへぐぢ")

	plaintext  = (u"helloworld",
		u"textnachtricht",
		u"unmensajedetexto",
		u"текст",
		u"だやぎへぐゆぢ")

	ciphertext = (u"danzqcwnnh",
		u"ßüowpsqöwbyfej",
		u"iyorrklrrbyrwylñ",
		u"шжуёш",
		u"だゆいれべやも")

	def test_encrypt(self):
		cipher = Beaufort()
		for i,alphabet in enumerate(self.alphabet):
			enc = cipher.encrypt(self.plaintext[i], self.key[i], alphabet)
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		cipher = Beaufort()
		for i,alphabet in enumerate(self.alphabet):
			dec = cipher.decrypt(self.ciphertext[i], self.key[i], alphabet)
			self.assertEqual(dec, self.plaintext[i])

if __name__ == '__main__': 
	unittest.main()
