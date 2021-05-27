#!/usr/bin/python
# -*- encoding: utf-8 -*-


from scytale import Scytale
import unittest


class TestScytale(unittest.TestCase):

    key = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    plaintext = "Iamhurtverybadlyhelp"

    ciphertext = ["Iamhurtverybadlyhelp",  # 1
                  "Imuteyalhlahrvrbdyep",  # 2
                  "Ihtraylauvydhpmreble",  # 3
                  "Iueaharrdemtyllhvbyp",  # 4
                  "Iryyatbhmvaehedlurlp",  # 5
                  "Italavdpmelhryuyhrbe",  # 6
                  "Ivlaeymrhhyeublraptd",  # 7
                  "Ieharemylhbpuardtlvy",  # 8
                  "Irlaypmbhaudrltyvhee",  # 9
                  "Iyabmahdulrythveelrp"]  # 10

    def test_encrypt(self):
        for i, k in enumerate(self.key):
            enc = Scytale().encrypt(self.plaintext, k)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, k in enumerate(self.key):
            dec = Scytale().decrypt(self.ciphertext[i], k)
            self.assertEqual(dec, self.plaintext)


if __name__ == '__main__':
    unittest.main()
