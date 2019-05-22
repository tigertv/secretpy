#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Bifid
from secretpy import alphabets
from unittest import TestCase, main


class TestBifid(TestCase):
    alphabet = (
        [
            u"b", u"g", u"w", u"k", u"z",
            u"q", u"p", u"n", u"d", u"s",
            u"ij", u"o", u"a", u"x", u"e",
            u"f", u"c", u"l", u"u", u"m",
            u"t", u"h", u"y", u"v", u"r"
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
        0,
        5,
        7,
        4,
        4,
        6,
    )

    plaintext = (
        u"fleeatonce",
        u"defendtheeastwallofthecastle",
        u"textnachtricht",
        u"unmensaiedetexto",
        u"текст",
        u"だやぎへぐゆぢ",
    )

    ciphertext = (
        u"uaeolwrins",
        u"ffyhmkhycpliashadtrlhcchlblr",
        u"qyldxscirbsrso",
        u"slxkobndadyyesxt",
        u"ни5чт",
        u"でげさでたどぢ",
    )

    def setUp(self):
        self.cipher = Bifid()

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
