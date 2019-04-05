#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot5
from unittest import TestCase, main


class TestRot5(TestCase):

    plaintext = (
        u"0123456789",
    )

    ciphertext = (
        u"5678901234",
    )

    cipher = Rot5()

    def test_encrypt(self):
        for i, plaintext in enumerate(self.plaintext):
            enc = self.cipher.encrypt(plaintext)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, plaintext in enumerate(self.plaintext):
            dec = self.cipher.decrypt(self.ciphertext[i])
            self.assertEqual(dec, plaintext)


if __name__ == '__main__':
    main()
