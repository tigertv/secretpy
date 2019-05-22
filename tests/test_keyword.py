#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Keyword
from secretpy import alphabets
import unittest


class TestKeyword(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH,
        alphabets.RUSSIAN,
        alphabets.GERMAN,
        alphabets.SPANISH,
        alphabets.JAPANESE_HIRAGANA
    )

    key = (
        u"kryptos",
        u"криптос",
        u"schlüssel",
        u"clave",
        u"やへぐぢ")

    plaintext = (
        u"knowledgeispower",
        u"знаниеэтосила",
        u"textnachtricht",
        u"unmensajedetexto",
        u"だやぎへぐゆぢ")

    ciphertext = (
        u"dghvetpstbmihvtl",
        u"бжкжвоэнзмвек",
        u"rüwrkshbrpdhbr",
        u"tmkemrchevesexsñ",
        u"つもくひけゆて")

    def test_encrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            enc = Keyword().encrypt(self.plaintext[i], self.key[i], alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            dec = Keyword().decrypt(self.ciphertext[i], self.key[i], alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
