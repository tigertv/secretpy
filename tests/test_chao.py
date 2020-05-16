#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Chao
from secretpy import alphabets
import unittest


class TestChao(unittest.TestCase):
    alphabet = (
        "ptlnbqdeoysfavzkgjrihwxumc",
        alphabets.ENGLISH,
        alphabets.RUSSIAN,
        alphabets.GERMAN,
        alphabets.SPANISH,
        alphabets.JAPANESE_HIRAGANA
    )

    key = (
        "hxuczvamdslkpefjrigtwobnyq",
        alphabets.ENGLISH,
        alphabets.RUSSIAN,
        alphabets.GERMAN,
        alphabets.SPANISH,
        alphabets.JAPANESE_HIRAGANA
    )

    plaintext = (
        u"text",
        u"donotusepc",
        u"съешьжеещёэтихмягкихфранцузскихбулокдавыпейчаю",
        u"textnachtricht",
        u"unmensajedetexto",
        u"だやぎへぐゆぢ"
    )

    ciphertext = (
        u"xawy",
        u"dnllqqymmw",
        u"сщгхшваясютъиъмосщюуаьйфрлмйкршузлмолъпеимвбйт",
        u"tdvqjzäblyßumw",
        u"umkbjñtdlxykwygñ",
        u"だもこはけみた"
    )

    def test_encrypt(self):
        c = Chao()
        for i, alphabet in enumerate(self.alphabet):
            enc = c.encrypt(self.plaintext[i], self.key[i], alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        c = Chao()
        for i, alphabet in enumerate(self.alphabet):
            dec = c.decrypt(self.ciphertext[i], self.key[i], alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
