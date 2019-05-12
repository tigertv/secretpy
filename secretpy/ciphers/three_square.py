#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .polybius_square import PolybiusSquare
import random


class ThreeSquare:
    """
    The Three Square Cipher
    """

    def __encDec(self, alphabet, text, key, isEncrypt):
        square1 = PolybiusSquare(alphabet, key[0])
        square2 = PolybiusSquare(alphabet, key[1])
        square3 = PolybiusSquare(alphabet, key[2])

        enc = u""
        if isEncrypt:
            if len(text) % 2:
                text += alphabet[-1][0]

            odd = text[1::2]
            even = text[::2]

            for i in range(len(even)):
                row1, column1 = square1.get_coordinates(even[i])
                row2, column2 = square2.get_coordinates(odd[i])

                rows = square1.get_rows()
                index = random.randrange(rows)
                left = square1.get_char(index, column1)

                middle = square3.get_char(row1, column2)

                cols = square2.get_columns()
                index = random.randrange(cols)
                right = square2.get_char(row2, index)

                enc += left + middle + right
        else:
            trigrams = []
            i = 0
            while i < len(text):
                trigrams.append(text[i:i+3])
                i += 3

            for trigram in trigrams:
                col1 = square1.get_coordinates(trigram[0])[1]
                row3, col3 = square3.get_coordinates(trigram[1])
                row2 = square2.get_coordinates(trigram[2])[0]
                enc += square1.get_char(row3, col1)
                enc += square2.get_char(row2, col3)
        return enc

    def encrypt(self, text, key=None, alphabet=None):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        alphabet = alphabet or [
            u"a", u"b", u"c", u"d", u"e",
            u"f", u"g", u"h", u"ij", u"k",
            u"l", u"m", u"n", u"o", u"p",
            u"q", u"r", u"s", u"t", u"u",
            u"v", u"w", u"x", u"y", u"z"
        ]
        return self.__encDec(alphabet, text, key, True)

    def decrypt(self, text, key=None, alphabet=None):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        alphabet = alphabet or [
            u"a", u"b", u"c", u"d", u"e",
            u"f", u"g", u"h", u"ij", u"k",
            u"l", u"m", u"n", u"o", u"p",
            u"q", u"r", u"s", u"t", u"u",
            u"v", u"w", u"x", u"y", u"z"
        ]
        return self.__encDec(alphabet, text, key, False)
