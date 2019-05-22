#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Polybius
from secretpy import alphabets
import unittest


class TestPolybius(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH_SQUARE_IJ,
        alphabets.GERMAN_SQUARE,
        alphabets.SPANISH_SQUARE,
        alphabets.RUSSIAN_SQUARE,
        alphabets.JAPANESE_HIRAGANA
    )

    plaintext = (
        u"sometextmessage",
        u"textnachtricht",
        u"unmensaiedetexto",
        u"текст",
        u"だやぎへぐゆぢ"
    )

    ciphertext = (
        u"231232245224255232242323314124",
        u"4521534535221213454432121345",
        u"51353414351512321423144514534541",
        u"4225114142",
        u"45771112137846",
    )

    key = (
        u"polybiusexample",
        u"schlüssel",
        u"llaves",
        u"ключи",
        u"ぎへぐ",
    )

    cipher = Polybius()

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
