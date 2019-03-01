#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Zigzag
import unittest


class TestZigzag(unittest.TestCase):
    key = (3, 4, 3, 3, 3, 3)

    plaintext = (
        u"wearediscoveredfleeatonce",
        u"defendtheeastwallofthecastle",
        u"текстовоесообщение",
        u"textnachtricht",
        u"unmensajedetexto",
        u"だやぎへぐゆぢ")

    ciphertext = (
        u"wecrlteerdsoeefeaocaivden",
        u"dttfsedhswotatfneaalhcleelee",
        u"ттебиесоосощнеквое",
        u"tnthetahrctxci",
        u"uneenesjdtxomaet",
        u"だぐやへゆぎぢ")

    def setUp(self):
        self.algorithm = Zigzag()

    def test_encrypt(self):
        for i, plaintext in enumerate(self.plaintext):
            enc = self.algorithm.encrypt(plaintext, self.key[i])
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, ciphertext in enumerate(self.ciphertext):
            dec = self.algorithm.decrypt(ciphertext, self.key[i])
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
