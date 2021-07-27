#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Bazeries
from secretpy import alphabets
import unittest


class TestBazeries(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH_SQUARE_IJ,
        alphabets.GERMAN_SQUARE,
        alphabets.SPANISH_SQUARE,
        alphabets.RUSSIAN_SQUARE,
        # alphabets.JAPANESE_HIRAGANA
    )

    key = (
        (81257, u"eightyonethousandtwohundredfiftyseven"),
        (234, u"zweidreivier"),
        (127, u"unodossiete"),
        (565, u"пятьшестьпять"),
        (443, u"ししさん"),
    )

    plaintext = (
        u"whoeverhasmadeavoyageupthehudsonmustrememberthekaatskillmountains",
        u"textnachtricht",
        u"unmensaiedetexto",
        u"текстздесь",
        u"だやぎへぐゆぢぢ"
    )

    ciphertext = (
        u"dumtmcdsenrtemveqxmoelccrvxdmdkwxnnmukrdkumynmbprkeepmgngekwxcrwb",
        u"sphplpgfznbpgf",
        u"ytglvmuhgvvvqpqk",
        u"2що02лщ0ца",
        u"れせもとねねわつ"
    )

    cipher = Bazeries()

    def test_encrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            enc = self.cipher.encrypt(self.plaintext[i], self.key[i], alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            dec = self.cipher.decrypt(self.ciphertext[i], self.key[i], alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
