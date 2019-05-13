#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import ThreeSquare
from secretpy import alphabets
import unittest
import sys

if sys.version_info[0] < 3:
    # Python 2
    from mock import patch, Mock
else:
    # Python 3
    from unittest.mock import patch, Mock


class TestThreeSquare(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH_SQUARE_NO_Z,
        alphabets.ENGLISH_SQUARE_IJ,
        alphabets.GERMAN_SQUARE,
        alphabets.SPANISH_SQUARE,
        alphabets.RUSSIAN_SQUARE,
        alphabets.JAPANESE_HIRAGANA
    )

    key = (
        (u"one", u"two", u"three"),
        (u"example", u"keyword", u"third"),
        (u"mein", u"schlüssel", u"drei"),
        (u"mis", u"llaves", u"tres"),
        (u"мой", u"ключ", u"три"),
        (u"だや", u"へぐ", u"ぢぢ"),
    )

    plaintext = (
        u"amessage",
        u"helpmeobiwankenobi",
        u"textnachtricht",
        u"unmensaiedetexto",
        u"текстздесь",
        u"だやぎへぐゆぢぢ"
    )

    ciphertext = (
        u"gtnftugqwgdd",
        u"bkelcndhelsdcmechndkefnebeg",
        u"fpadzpfracfcftpdrcbop",
        u"guicsafmafriedcegpedwfnp",
        u"когкгтксгджгзощ",
        u"くかまぎけぐぐさまぐづつ",
    )

    cipher = ThreeSquare()

    @patch('random.randrange')
    def test_encrypt(self, randrange):
        randrange.return_value = 1
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
