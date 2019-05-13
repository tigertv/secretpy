#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import TwoSquare
from secretpy import alphabets
import unittest


class TestTwoSquare(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH_SQUARE_IJ,
        alphabets.GERMAN_SQUARE,
        alphabets.SPANISH_SQUARE,
        alphabets.RUSSIAN_SQUARE,
        alphabets.JAPANESE_HIRAGANA
    )

    key = (
        (u"example", u"keyword"),
        (u"mein", u"schlüssel"),
        (u"mis", u"llaves"),
        (u"мой", u"ключ"),
        (u"だや", u"へぐ"),
    )

    plaintext = (
        u"helpmeobiwankenobi",
        u"textnachtricht",
        u"unmensaiedetexto",
        u"текстздесь",
        u"だやぎへぐゆぢぢ"
    )

    ciphertext = (
        u"xgcmxwsrkyxphwpldg",
        u"qdzqeddctrehpo",
        u"otaloeimedgqxdpr",
        u"рзгцкржгрэ",
        u"おぽくうごもぢぢ"
    )

    cipher = TwoSquare()

    def test_encrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            enc = self.cipher.encrypt(self.plaintext[i], self.key[i], alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            dec = self.cipher.decrypt(self.ciphertext[i],
                                      self.key[i], alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
