#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Vigenere
from secretpy import alphabets
import unittest


class TestVigenere(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH,
        alphabets.RUSSIAN,
        alphabets.GERMAN,
        alphabets.SPANISH,
        alphabets.JAPANESE_HIRAGANA
    )

    key = (
        u"lemon",
        u"ключ",
        u"schlüssel",
        u"clave",
        u"やへぐぢ")

    plaintext = (
        u"attackatdawn",
        u"текст",
        u"textnachtricht",
        u"unmensajedetexto",
        u"だやぎへぐゆぢ")

    ciphertext = (
        u"lxfopvefrnhr",
        u"эрииэ",
        u"hgaalsulafkjsr",
        u"wxmzquljzhgeesxq",
        u"ぐたぜぁゅちへ")

    def test_encrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            enc = Vigenere().encrypt(self.plaintext[i], self.key[i], alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            dec = Vigenere().decrypt(self.ciphertext[i], self.key[i], alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
