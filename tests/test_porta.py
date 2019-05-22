#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Porta
from secretpy import alphabets
import unittest


class TestPorta(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH,
        alphabets.ENGLISH,
        alphabets.RUSSIAN,
        alphabets.GERMAN,
        alphabets.SPANISH,
    )

    key = (
        u"fortification",
        u"lemon",
        u"ключ",
        u"schlüssel",
        u"clave",
    )

    plaintext = (
        u"defendtheeastwallofthecastle",
        u"attackatdawn",
        u"текст",
        u"textnachtricht",
        u"unmensajedetexto",
    )

    ciphertext = (
        u"synnjscvrnrlahutukucvryrlany",
        u"seauvppaxtel",
        u"нъщён",
        u"kufoöyäyoiyuöf",
        u"hiyolfrvorrcqafb",
    )

    cipher = Porta()

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
