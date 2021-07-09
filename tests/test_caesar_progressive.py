#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import CaesarProgressive
from secretpy import alphabets
import unittest


class TestCaesarProgressive(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH,
        alphabets.RUSSIAN,
        alphabets.GERMAN,
        alphabets.SPANISH,
        alphabets.JAPANESE_HIRAGANA
    )

    key = (3, 9, 7, 4, 13)

    plaintext = (
        u"thequickbrownfoxjumpsoverthelazydog",
        u"съешьжеещёэтихмягкихфранцузскихбулокдавыпейчаю",
        u"textnachtricht",
        u"unmensajedetexto",
        u"だやぎへぐゆぢ"
    )

    ciphertext = (
        u"wljwbqlumdbkcvfpcohlpmuesvkiqgggmyr",
        u"ъдпдифуфйчпёэкгцыдгррнюмцфйфонызыфшхпмпйяхыйут",
        u"ämcßympvedzuäj",
        u"yrrlubktppritñlh",
        u"へぁちもとえぱ"
    )

    cipher = CaesarProgressive()

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
