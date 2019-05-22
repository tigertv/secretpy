#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Playfair
from secretpy import alphabets
import unittest


class TestPlayfair(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH_SQUARE_IJ,
        alphabets.ENGLISH_SQUARE_IJ,
        alphabets.GERMAN_SQUARE,
        alphabets.SPANISH_SQUARE,
    )

    key = (
        u"wheatson",
        u"playfireexample",
        u"schlüssel",
        u"llaves",

        u"ключи",
        u"ぎへぐ"
    )

    plaintext = (
        u"idiocyoftenlookslikeintelligence",
        u"hidethegoldinthetreestump",
        u"textnachtricht",
        u"unmensaiedetexto",

        u"текстсообщение",
        u"だやぎへぐゆぢ",
    )

    ciphertext = (
        u"kffbbzfmwaspnvcfdukdagcewpqdpnbsne",
        u"bmodzbxdnabekudmuixmmouvif",
        u"ofzqifhlotpauq",
        u"zhrftgcpvfsrvyop",

        u"хвбшутр3здэвпюж4",
        u"222222",
    )

    cipher = Playfair()

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
