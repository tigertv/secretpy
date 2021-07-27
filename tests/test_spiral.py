#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Spiral, alphabets as al
import unittest


class TestSpiral(unittest.TestCase):
    alphabet = (
        al.ENGLISH,
        al.ENGLISH,
        al.ENGLISH,
        al.ENGLISH,
        al.ENGLISH,
        # al.GERMAN,
        # al.SPANISH,
    )

    key = (
        3,
        5,
        5,
        5,
        5,
    )

    plaintext = (
        u"wearediscoveredfleeatoncejx",     # no remainder
        u"wearediscoveredfleeatoncejck",    # with remainder
        u"wearediscoveredfleeatoncejckxx",  # no remainder
        u"manifolds",                       # with remainder key - 1
        u"manif",                           # one line, no remainder
        u"mani",                            # one line, with remainder
        u"m",                               # one char, with remainder
        u"",                                # empty
    )

    ciphertext = (
        u"ejxctedecdaewriorfeonalevse",
        u"jckeadoeraewdvftonceecsieler",
        u"jckxxeadoeraewdvftonceecsieler",
        u"oldsfinam",
        u"manif",
        u"mani",
        u"",
    )

    cipher = Spiral()

    def test_encrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            enc = self.cipher.encrypt(
                self.plaintext[i], self.key[i], alphabet)
            self.assertEqual(enc, self.ciphertext[i])

    def test_decrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            dec = self.cipher.decrypt(
                self.ciphertext[i], self.key[i], alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
