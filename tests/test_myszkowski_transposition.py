#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import MyszkowskiTransposition
from secretpy import alphabets
import unittest


class TestMyszkowskiTransposition(unittest.TestCase):

    alphabet = (
        alphabets.ENGLISH,
        alphabets.ENGLISH,
    )

    key = (
        u"tomato",
        u"german",
    )

    plaintext = (
        u"wearediscoveredfleeatonce",
        u"defendtheeastwallofthecastlexx",
    )

    ciphertext = (
        u"rofoacdtedseeeacweivrlene",
        u"nalcxehwttdttfseeleedsoaxfeahl",
    )

    cipher = MyszkowskiTransposition()

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
