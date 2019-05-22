#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Atbash
from secretpy import alphabets
import unittest


class TestAtbash(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH,
        alphabets.RUSSIAN,
        alphabets.GERMAN,
        alphabets.SPANISH,
        alphabets.JAPANESE_HIRAGANA
    )

    key = 0

    plaintext = (
        u"text",
        u"текст",
        u"textnachtricht",
        u"unmensajedetexto",
        u"だやぎへぐゆぢ")

    ciphertext = (
        u"gvcg",
        u"мъфнм",
        u"kzgkqßöwkmvöwk",
        u"fnñvnhzqvwvgvcgl",
        u"ぶすれどるしび")

    def test_encrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            enc = Atbash().encrypt(self.plaintext[i], self.key, alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            dec = Atbash().decrypt(self.ciphertext[i], self.key, alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
