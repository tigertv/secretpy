#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Caesar
import unittest

class TestCaesar(unittest.TestCase):
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

	key = (-3,3,3,3,3)

	plaintext  = (u"thequickbrownfoxjumpsoverthelazydog",
		u"съешьжеещёэтихмягкихфранцузскихбулокдавыпейчаю",
		u"textnachtricht",
		u"unmensajedetexto",
		u"だやぎへぐゆぢ")

	ciphertext = (u"qebnrfzhyoltkclugrjmplsboqebixwvald",
		u"фэзыяйззьиахлшпвёнлшчугрщцкфнлшдцоснжгеютзмъгб",
		u"whäwqdfkwulfkw",
		u"xpohpvdmhghwhawr",
		u"でらごびさりど")

	def test_encrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			enc = Caesar().encrypt(self.plaintext[i], self.key[i], alphabet)
			self.assertEqual(enc, self.ciphertext[i])

	def test_decrypt(self):
		for i,alphabet in enumerate(self.alphabet):
			dec = Caesar().decrypt(self.ciphertext[i], self.key[i], alphabet)
			self.assertEqual(dec, self.plaintext[i])

if __name__ == '__main__': 
	unittest.main()
