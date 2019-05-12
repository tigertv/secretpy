#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import ThreeSquare
import unittest
import sys

if sys.version_info[0] < 3:
    # Python 2
    from mock import patch, Mock
else:
    # Python 3
    from unittest.mock import patch, Mock


class TestThreeSquare(unittest.TestCase):
    alphabet = (
        (
            u"a", u"b", u"c", u"d", u"e",
            u"f", u"g", u"h", u"i", u"j",
            u"k", u"l", u"m", u"n", u"o",
            u"p", u"q", u"r", u"s", u"t",
            u"u", u"v", u"w", u"x", u"y",
        ),
        (
            u"a", u"b", u"c", u"d", u"e",
            u"f", u"g", u"h", u"ij", u"k",
            u"l", u"m", u"n", u"o", u"p",
            u"q", u"r", u"s", u"t", u"u",
            u"v", u"w", u"x", u"y", u"z",
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
            u"щ", u"ы", u"ьъ", u"э", u"ю", u"я",
            u"0", u"1", u"2", u"3", u"4", u"5",
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
        (u"one", u"two", u"three"),
        (u"example", u"keyword", u"third"),
        (u"mein", u"schlüssel", u"drei"),
        (u"mis", u"llaves", u"tres"),
        (u"мой", u"ключ", u"три"),
        (u"だや", u"へぐ", u"ぢぢ"),
    )

    plaintext = (
        u"amessage",
        u"helpmeobiwankenobi",
        u"textnachtricht",
        u"unmensaiedetexto",
        u"текстздесь",
        u"だやぎへぐゆぢぢ"
    )

    ciphertext = (
        u"gtnftugqwgdd",
        u"bkelcndhelsdcmechndkefnebeg",
        u"fpadzpfracfcftpdrcbop",
        u"guicsafmafriedcegpedwfnp",
        u"когкгтксгджгзощ",
        u"くかまぎけぐぐさまぐづつ",
    )

    cipher = ThreeSquare()

    @patch('random.randrange')
    def test_encrypt(self, randrange):
        randrange.return_value = 1
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
