#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Enigma, alphabets
import unittest


class TestEnigma(unittest.TestCase):
    alphabet = (
        alphabets.ENGLISH,
        alphabets.ENGLISH,
        # alphabets.RUSSIAN,
        # alphabets.GERMAN,
        # alphabets.SPANISH,
        # alphabets.JAPANESE_HIRAGANA
    )

    keys = (
        {
            'reflector': 'B',
            'rotor_offsets': ('c', 'a', 't'),  # Grundstellung
            'ring_offsets': ('k', 'e', 'y'),   # Ringstellung
            'rotor_order': (1, 2, 3),
            'steckers': [('v', 'b'), ('z', 'w')]
        },
        {
            'reflector': 'C',
            'rotor_offsets': ('c', 'c', 'c'),  # Grundstellung
            'ring_offsets': ('k', 'e', 'y'),   # Ringstellung
            'rotor_order': (5, 3, 4),
            'steckers': [('v', 'b'), ('z', 'w'), ('y', 'j')]
        },
    )

    plaintext = (
        u"thequickbrownfoxjumpsoverthelazydog",
        u"thequickbrownfoxjumpsoverthelazydog",
        #
        u"съешьжеещёэтихмягкихфранцузскихбулокдавыпейчаю",
        u"textnachtricht",
        u"unmensajedetexto",
        u"あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをんゃゅょぁぇ"
    )

    ciphertext = (
        u"fdcelvalieivlvujgfvsfrstelrunbigbeu",
        u"nguxngzdyhpmglkmwsxlglyjobudofcoclz",
        #
        u"фэзыяйззьиахлшпвёнлшчугрщцкфнлшдцоснжгеютзмъгб",
        u"whäwqdfkwulfkw",
        u"xpohpvdmhghwhawr",
        u"えおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをんゃゅょぁぇあいう"
    )

    __cipher = Enigma()

    def test_encrypt(self):
        for a, p, k, c in zip(self.alphabet, self.plaintext, self.keys, self.ciphertext):
            enc = self.__cipher.encrypt(p, k, a)
            self.assertEqual(enc, c)

    def test_decrypt(self):
        for i, alphabet in enumerate(self.alphabet):
            dec = self.__cipher.decrypt(self.ciphertext[i], self.keys[i], alphabet)
            self.assertEqual(dec, self.plaintext[i])


if __name__ == '__main__':
    unittest.main()
