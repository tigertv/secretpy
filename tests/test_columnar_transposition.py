#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import ColumnarTransposition
from secretpy import alphabets
import unittest


class TestColumnarTransposition(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH,
        alphabets.ENGLISH,
        alphabets.ENGLISH,
        alphabets.GERMAN,
        alphabets.SPANISH,
    )

    key = (
        u"zebras",
        u"zebras",
        u"german",
        u"schlüssel",
        u"clave",
    )

    plaintext = (
        u"wearediscoveredfleeatonceqkjeu",
        u"wearediscoveredfleeatonce",
        u"defendtheeastwallofthecastlexx",
        u"textnachtricht",
        u"unmensaiedetexto",
    )

    ciphertext = (
        u"evlneacdtkeseaqrofojdeecuwiree",
        u"evlnacdtesearofodeecwiree",
        u"nalcxehwttdttfseeleedsoaxfeahl",
        u"eihxcthttracnt",
        u"mieuseondtnateex",
    )

    cipher = ColumnarTransposition()

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
