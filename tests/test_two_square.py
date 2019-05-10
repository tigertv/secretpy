#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import TwoSquare
import unittest


class TestTwoSquare(unittest.TestCase):
    alphabet = (
        (
            u"a", u"b", u"c", u"d", u"e",
            u"f", u"g", u"h", u"ij", u"k",
            u"l", u"m", u"n", u"o", u"p",
            u"q", u"r", u"s", u"t", u"u",
            u"v", u"w", u"x", u"y", u"z",
        ),
        (
            u"p", u"l", u"a", u"y", u"f",
            u"ij", u"r", u"e", u"x", u"m",
            u"b", u"c", u"d", u"g", u"h",
            u"k", u"n", u"o", u"q", u"s",
            u"t", u"u", u"v", u"w", u"z",
        ),
        (
            u"aä", u"b", u"c", u"d", u"e",
            u"f", u"g", u"h", u"ij", u"k",
            u"l", u"m", u"n", u"oö", u"p",
            u"q", u"r", u"sß", u"t", u"uü",
            u"v", u"w", u"x", u"y", u"z"
        ),
        (
            u"a", u"b", u"c", u"d", u"e",
            u"f", u"g", u"h", u"ij", u"k",
            u"l", u"m", u"nñ", u"o", u"p",
            u"q", u"r", u"s", u"t", u"u",
            u"v", u"w", u"x", u"y", u"z"
        ),
        (
            u"а", u"б", u"в", u"г", u"д", u"её",
            u"ж", u"з", u"ий", u"к", u"л", u"м",
            u"н", u"о", u"п", u"р", u"с", u"т",
            u"у", u"ф", u"х", u"ц", u"ч", u"ш",
            u"щ", u"ы", u"ьъ", u"э", u"ю", u"я"
        ),
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
        ),
    )

    key = (
        (u"example", u"keyword"),
        (u"example", u"keyword"),
        (u"mein", u"schlüssel"),
        (u"mis", u"llaves"),
        (u"мой", u"ключ"),
        (u"だや", u"へぐ"),
    )

    plaintext = (
        u"helpmeobiwankenobi",
        u"hidethegoldinthetreestumps",
        u"textnachtricht",
        u"unmensaiedetexto",
        u"текстздесь",
        u"だやぎへぐゆぢぢ"
    )

    ciphertext = (
        u"xgcmxwsrkyxphwpldg",
        u"cbcyvcxcqpcxugcolsxknzwiez",
        u"qdzqeddctrehpo",
        u"otaloeimedgqxdpr",
        u"рзгцкржгрэ",
        u"おぽくうごもぢぢ"
    )

    cipher = TwoSquare()

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
