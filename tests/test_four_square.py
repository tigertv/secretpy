#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import FourSquare
from secretpy import alphabets
import unittest


class TestFourSquare(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH_SQUARE_IJ,
        alphabets.ENGLISH_SQUARE_OQ,
        alphabets.GERMAN_SQUARE,
        alphabets.SPANISH_SQUARE,
        alphabets.RUSSIAN_SQUARE,
        alphabets.JAPANESE_HIRAGANA
    )

    key = (
        (u"criptog", u"segurt"),
        (u"example", u"keyword"),
        (u"mein", u"schlüssel"),
        (u"mis", u"llaves"),
        (u"мой", u"ключ"),
        (u"だや", u"へぐ"),
    )

    plaintext = (
        u"attackatdawn",
        u"helpmeobiwankenobi",
        u"textnachtricht",
        u"unmensaiedetexto",
        u"текстздесь",
        u"だやぎへぐゆぢぢ"
    )

    ciphertext = (
        u"pmmutbpmcuxh",
        u"fygmkyhobxmfkkkimd",
        u"ulyqhhibrrdlfq",
        u"rnoalqabasatsztm",
        u"тбзонзвапэ",
        u"づむごぬごむとだ"
    )

    cipher = FourSquare()

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
