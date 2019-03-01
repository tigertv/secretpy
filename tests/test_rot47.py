#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot47
from unittest import TestCase, main


class TestRot47(TestCase):

    plaintext = (
        u"agirlhas>12345cats",
        u"Thegirlhas>12345dogs",
    )

    ciphertext = (
        u"28:C=92Dm`abcd42ED",
        u"%968:C=92Dm`abcd5@8D",
    )

    cipher = Rot47()

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
