#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import ADFGX
from secretpy import alphabets
import unittest


class TestADFGX(unittest.TestCase):
    alphabet = (
        [
            u"b", u"t", u"a", u"l", u"p",
            u"d", u"h", u"o", u"z", u"k",
            u"q", u"f", u"v", u"s", u"n",
            u"g", u"ij", u"c", u"u", u"x",
            u"m", u"r", u"e", u"w", u"y"
        ],
        alphabets.GERMAN_SQUARE,
        alphabets.SPANISH_SQUARE,
    )

    key = (
        u"cargo",
        u"schlussel",
        u"clave",
    )

    plaintext = (
        u"attackatonce",
        u"textnachtricht",
        u"unmensaiedetexto",
    )

    ciphertext = (
        u"faxdfadddgdgfffafaxafafx",
        u"gadggfaadxagfgggfggfdfgfdxfa",
        u"fxaxgfgdggaxfffdgagxafaxxgffaagg",
    )

    cipher = ADFGX()

    def test_encrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            enc = self.cipher.encrypt(
                self.plaintext[i], self.key[i], alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            dec = self.cipher.decrypt(
                self.ciphertext[i], self.key[i], alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
