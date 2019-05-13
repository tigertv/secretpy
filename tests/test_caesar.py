#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Caesar
from secretpy import alphabets
import unittest


class TestCaesar(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH,
        alphabets.RUSSIAN,
        alphabets.GERMAN,
        alphabets.SPANISH,
        alphabets.JAPANESE_HIRAGANA
    )

    key = (-3, 3, 3, 3, 3)

    plaintext = (
        u"thequickbrownfoxjumpsoverthelazydog",
        u"съешьжеещёэтихмягкихфранцузскихбулокдавыпейчаю",
        u"textnachtricht",
        u"unmensajedetexto",
        u"だやぎへぐゆぢ")

    ciphertext = (
        u"qebnrfzhyoltkclugrjmplsboqebixwvald",
        u"фэзыяйззьиахлшпвёнлшчугрщцкфнлшдцоснжгеютзмъгб",
        u"whäwqdfkwulfkw",
        u"xpohpvdmhghwhawr",
        u"でらごびさりど")

    def test_encrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            enc = Caesar().encrypt(self.plaintext[i], self.key[i], alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            dec = Caesar().decrypt(self.ciphertext[i], self.key[i], alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
