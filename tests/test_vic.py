#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Vic
from unittest import TestCase, main


class TestVic(TestCase):
    alphabet = (
        [
            u"e", u"t", u"", u"a", u"o", u"n", u"", u"r", u"i", u"s",
            u"b", u"c", u"d", u"f", u"g", u"h", u"j", u"k", u"l", u"m",
            u"p", u"q", u"/", u"u", u"v", u"w", u"x", u"y", u"z", u".",
        ],
    )

    key = (
        u"0452",
    )

    plaintext = (
        u"attackatdawn",
    )

    ciphertext = (
        u"anwhrsanroaeer",
    )

    def setUp(self):
        self.cipher = Vic()

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
