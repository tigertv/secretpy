#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Affine
import unittest

class TestAffine(unittest.TestCase):
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

	key = ([5,8],[5,8],[7,8],[5,8],[5,8])

	plaintext = (u"affinecipher",
		u"текст",
		u"textnachtricht",
		u"unmensajedetexto",
		u"だやぎへぐゆぢ")

	ciphertext = (u"ihhwvcswfrcp",
		u"даэяд",
		u"vgtvjiwövhewöv",
		u"fsñbsvizbwbabtac",
		u"うぁらろわいく")

	def test_encrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			enc = Affine().encrypt(self.plaintext[i], self.key[i], alphabet)
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			dec = Affine().decrypt(self.ciphertext[i], self.key[i], alphabet)
			self.assertEqual(dec, self.plaintext[i])

if __name__ == '__main__': 
	unittest.main()
