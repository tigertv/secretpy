#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy.rot13 import Rot13
import unittest

class TestRot13(unittest.TestCase):
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

	plaintext  = (
		u"whydidthechickencrosstheroad",
		u"текст",
		u"textnachtricht",
		u"unmensajedetexto",
		u"だやぎへぐゆぢ"
	)

	ciphertext = (
		u"julqvqgurpuvpxrapebffgurebnq",
		u"вхыбв",
		u"etieüprwecxrwe",
		u"hnzrnfñwrqrgrkgb",
		u"をじぱおぴずん"
	)

	def test_encrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			enc = Rot13().encrypt(self.plaintext[i], self.key, alphabet)
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			dec = Rot13().decrypt(self.ciphertext[i], self.key, alphabet)
			self.assertEqual(dec, self.plaintext[i])

if __name__ == '__main__': 
	unittest.main()
