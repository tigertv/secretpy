#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy.autokey import Autokey
import unittest

class TestAutokey(unittest.TestCase):
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

	key = (u"queenly",
		u"ключ",
		u"schlüssel",
		u"clave",
		u"やへぐぢ")

	plaintext  = (u"attackatdawn",
		u"текст",
		u"textnachtricht",
		u"unmensajedetexto",
		u"だやぎへぐゆぢ")

	ciphertext = (u"qnxepvytwtwp",
		u"эриие",
		u"hgaalsulagmzäc",
		u"wxmzqnnuipwtnbws",
		u"ぐたぜぁふへふ")

	def test_encrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			enc = Autokey().encrypt(self.key[i], self.plaintext[i], alphabet)
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			dec = Autokey().decrypt(self.key[i], self.ciphertext[i], alphabet)
			self.assertEqual(dec, self.plaintext[i])

if __name__ == '__main__': 
	unittest.main()
