#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Autokey
from secretpy import alphabets
import unittest


class TestAutokey(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH,
        alphabets.RUSSIAN,
        alphabets.GERMAN,
        alphabets.SPANISH,
        alphabets.JAPANESE_HIRAGANA
    )

    key = (
        u"queenly",
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
        u"qnxepvytwtwp",
        u"эриие",
        u"hgaalsulagmzäc",
        u"wxmzqnnuipwtnbws",
        u"ぐたぜぁふへふ")

    def test_encrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            enc = Autokey().encrypt(self.plaintext[i], self.key[i], alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            dec = Autokey().decrypt(self.ciphertext[i], self.key[i], alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
