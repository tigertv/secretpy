#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Atbash
import unittest

class TestAtbash(unittest.TestCase):
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

	key = 0

	plaintext = (u"text",
		u"текст",
		u"textnachtricht",
		u"unmensajedetexto",
		u"だやぎへぐゆぢ")

	ciphertext = (u"gvcg",
		u"мъфнм",
		u"kzgkqßöwkmvöwk",
		u"fnñvnhzqvwvgvcgl",
		u"ぶすれどるしび")

	def test_encrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			enc = Atbash().encrypt(self.plaintext[i], self.key, alphabet)
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			dec = Atbash().decrypt(self.ciphertext[i], self.key, alphabet)
			self.assertEqual(dec, self.plaintext[i])

if __name__ == '__main__': 
	unittest.main()
