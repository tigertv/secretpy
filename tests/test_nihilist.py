#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Nihilist
from secretpy import alphabets
from unittest import TestCase, main


class TestNihilist(TestCase):
    alphabet = (
        [
            u"z", u"e", u"b", u"r", u"a",
            u"s", u"c", u"d", u"f", u"g",
            u"h", u"ij", u"k", u"l", u"m",
            u"n", u"o", u"p", u"q", u"t",
            u"u", u"v", u"w", u"x", u"y"
        ],
        [
            u"p", u"h", u"q", u"g", u"m",
            u"e", u"a", u"y", u"l", u"n",
            u"o", u"f", u"d", u"x", u"k",
            u"r", u"c", u"v", u"s", u"z",
            u"w", u"b", u"u", u"t", u"ij"
        ],
        alphabets.GERMAN_SQUARE,
        alphabets.SPANISH_SQUARE,
        alphabets.RUSSIAN_SQUARE,
        alphabets.JAPANESE_HIRAGANA
    )

    key = (
        u"russian",
        u"akey",
        u"gkey",
        u"skey",
        u"ключ",
        u"あう",
    )

    plaintext = (
        u"dynamitewinterpalace",
        u"defendtheeastwallofthecastle",
        u"textnachtricht",
        u"unmensaiedetexto",
        u"текст",
        u"だやぎへぐゆぢ",
    )

    ciphertext = (
        u"37 106 62 36 67 47 86 26 104 53 62 77 27 55 57 66 55 36 54 27",
        u"55 56 53 44 47 68 75 35 43 56 43 67 76 86 43 47 46 66 53 77 34 56 63"
        " 45 66 89 45 44",
        u"66 40 68 98 55 36 28 77 66 67 39 67 45 69",
        u"88 58 47 69 76 68 26 78 58 39 30 98 58 78 59 88",
        u"60 41 79 80 60",
        u"55 90 34 71 35 91 56",
    )

    def setUp(self):
        self.cipher = Nihilist()

    def test_encrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            enc = self.cipher.encrypt(self.plaintext[i], self.key[i], alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            dec = self.cipher.decrypt(
                self.ciphertext[i], self.key[i], alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    main()
