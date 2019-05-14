#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import ColumnarTransposition
from secretpy import alphabets
import unittest


class TestColumnarTransposition(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH,
    )

    key = (
        u"zebras",
        u"german",
        u"schlüssel",
        u"clave",
    )

    plaintext = (
        u"wearediscoveredfleeatonceqkjeu",
        u"defendtheeastwallofthecastlexx",
        u"textnachtricht",
        u"unmensaiedetexto",
    )

    ciphertext = (
        u"evlneacdtkeseaqrofojdeecuwiree",
        u"nalcxehwttdttfseeleedsoaxfeahl",
        u"111111111",
        u"222222222222222",
    )

    chipher = ColumnarTransposition()

    def test_encrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            enc = self.chipher.encrypt(
                self.plaintext[i], self.key[i], alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            dec = self.chipher.decrypt(
                self.ciphertext[i], self.key[i], alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
