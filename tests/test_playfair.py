#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Playfair
import unittest


class TestPlayfair(unittest.TestCase):
    alphabet = (
        [
            u"w", u"h", u"e", u"a", u"t",
            u"s", u"o", u"n", u"b", u"c",
            u"d", u"f", u"g", u"ij", u"k",
            u"l", u"m", u"p", u"q", u"r",
            u"u", u"v", u"x", u"y", u"z"
        ],
        [
            u"p", u"l", u"a", u"y", u"f",
            u"ij", u"r", u"e", u"x", u"m",
            u"b", u"c", u"d", u"g", u"h",
            u"k", u"n", u"o", u"q", u"s",
            u"t", u"u", u"v", u"w", u"z",
        ],
    )

    """
        [u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"ij", u"k", u"l",
         u"m", u"n", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w",
        u"x", u"y", u"z"],

        [u"aä", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"ij", u"k", u"l",
         u"m", u"n", u"oö", u"p", u"q", u"r", u"sß", u"t", u"uü", u"v", u"w",
         u"x", u"y", u"z"],
        [u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"ij", u"k", u"l",
         u"m", u"nñ", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w",
         u"x", u"y", u"z"],
        [u"а", u"б", u"в", u"г", u"д", u"её", u"ж", u"з", u"ий", u"к", u"л",
         u"м", u"н", u"о", u"п", u"р", u"с", u"т", u"у", u"ф", u"х", u"ц",
         u"ч", u"ш", u"щ", u"ы", u"ьъ", u"э", u"ю", u"я"],
        (
            u"あいうえお"
            u"かきくけこ"
            u"がぎぐげご"
            u"さしすせそ"
            u"ざじずぜぞ"
            u"たちつてと"
            u"だぢづでど"
            u"なにぬねの"
            u"はひふへほ"
            u"ばびぶべぼ"
            u"ぱぴぷぺぽ"
            u"まみむめも"
            u"やゆよ"
            u"らりるれろ"
            u"わを"
            u"ん"
            u"ゃゅょぁぇ"
            u"じづ"
        )
    )
    """

    key = (
        u"",
        u"",
        u"",
        u"",
        u"")

    plaintext = (
        u"idiocyoftenlookslikeintelligence",
        u"hidethegoldinthetreestump",

        u"textnachtricht",
        u"unmensaiedetexto",
        u"текст",
        u"だやぎへぐゆぢ")

    ciphertext = (
        u"kffbbzfmwaspnvcfdukdagcewpqdpnbsne",
        u"bmodzbxdnabekudmuixmmouvif",

        u"4415534433111323444224132344",
        u"45333215334311241514154415534434",
        u"3616243536",
        u"44772358247845")

    cipher = Playfair()

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
