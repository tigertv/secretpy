#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .polybius_square import PolybiusSquare


class TwoSquare:
    """
    The Two-Square Cipher
    """

    def __enc(self, alphabet, text, key):
        square1 = PolybiusSquare(alphabet, key[0])
        square2 = PolybiusSquare(alphabet, key[1])

        # text encryption
        if len(text) % 2:
            text += alphabet[-1][0]
        odd = text[1::2]
        even = text[::2]
        enc = u""

        for i in range(len(even)):
            coords = square1.get_coordinates(even[i])
            row1 = coords[0]
            column1 = coords[1]

            coords = square2.get_coordinates(odd[i])
            row2 = coords[0]
            column2 = coords[1]

            if column1 == column2:
                enc += square1.get_char(row2, column1)
                enc += square2.get_char(row1, column1)
            else:
                enc += square1.get_char(row1, column2)
                enc += square2.get_char(row2, column1)
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
        return self.__enc(alphabet, text, key)

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
        return self.__enc(alphabet, text, key)
