#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy.zigzag import Zigzag
import unittest

class TestZigzag(unittest.TestCase):
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

	key = (3,3,3,3,3) 

	plaintext = (u"wearediscoveredfleeatonce",
		u"текстовоесообщение",
		u"textnachtricht",
		u"unmensajedetexto",
		u"だやぎへぐゆぢ")

	ciphertext = (u"wecrlteerdsoeefeaocaivden",
		u"ттебиесоосощнеквое",
		u"tnthetahrctxci",
		u"uneenesjdtxomaet",
		u"だぐやへゆぎぢ")

	def test_encrypt(self):
		algorithm = Zigzag() 
		for i,alphabet in enumerate(self.alphabet):
			enc = algorithm.encrypt(self.key[i], self.plaintext[i], alphabet)
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		algorithm = Zigzag() 
		for i,alphabet in enumerate(self.alphabet):
			dec = algorithm.decrypt(self.key[i], self.ciphertext[i], alphabet)
			self.assertEqual(dec, self.plaintext[i])

if __name__ == '__main__': 
	unittest.main()
