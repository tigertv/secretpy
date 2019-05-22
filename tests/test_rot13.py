#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot13
from secretpy import alphabets
from unittest import TestCase, main


class TestRot13(TestCase):
    alphabet = (
        alphabets.ENGLISH,
        alphabets.RUSSIAN,
        alphabets.GERMAN,
        alphabets.SPANISH,
        alphabets.JAPANESE_HIRAGANA
    )

    key = 0

    plaintext = (
        u"whydidthechickencrosstheroad",
        u"текст",
        u"textnachtricht",
        u"unmensajedetexto",
        u"だやぎへぐゆぢ"
    )

    ciphertext = (
        u"julqvqgurpuvpxrapebffgurebnq",
        u"вхыбв",
        u"etieüprwecxrwe",
        u"hnzrnfñwrqrgrkgb",
        u"をじぱおぴずん"
    )

    cipher = Rot13()

    def test_encrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            enc = self.cipher.encrypt(self.plaintext[i], self.key, alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            dec = self.cipher.decrypt(self.ciphertext[i], self.key, alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    main()
