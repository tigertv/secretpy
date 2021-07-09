#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Beaufort
from secretpy import alphabets
import unittest


class TestBeaufort(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH,
        alphabets.GERMAN,
        alphabets.SPANISH,
        alphabets.RUSSIAN,
        alphabets.JAPANESE_HIRAGANA
    )

    key = (
        u"key",
        u"schlüssel",
        u"clave",
        u"ключ",
        u"やへぐぢ")

    plaintext = (
        u"helloworld",
        u"textnachtricht",
        u"unmensajedetexto",
        u"текст",
        u"だやぎへぐゆぢ")

    ciphertext = (
        u"danzqcwnnh",
        u"ßüowpsqöwbyfej",
        u"iyorrklrrbyrwylñ",
        u"шжуёш",
        u"だもいりべめむ")

    def test_encrypt(self):
        cipher = Beaufort()
        for i, alphabet in enumerate(self.alphabet):
            enc = cipher.encrypt(self.plaintext[i], self.key[i], alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        cipher = Beaufort()
        for i, alphabet in enumerate(self.alphabet):
            dec = cipher.decrypt(self.ciphertext[i], self.key[i], alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
