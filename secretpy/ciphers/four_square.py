#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .polybius_square import PolybiusSquare


class FourSquare:
    """
    The Four-Square Cipher
    """

    def __enc(self, alphabet, text, key, isEncrypt):
        square01 = PolybiusSquare(alphabet, key[0])
        square10 = PolybiusSquare(alphabet, key[1])
        square = PolybiusSquare(alphabet, "")

        # text encryption
        if len(text) % 2:
            text += alphabet[-1][0]
        odd = text[1::2]
        even = text[::2]
        enc = u""
        if isEncrypt:
            for i in range(len(even)):
                coords = square.get_coordinates(even[i])
                row00 = coords[0]
                column00 = coords[1]

                coords = square.get_coordinates(odd[i])
                row11 = coords[0]
                column11 = coords[1]

                enc += square01.get_char(row00, column11)
                enc += square10.get_char(row11, column00)
        else:
            for i in range(len(even)):
                coords = square01.get_coordinates(even[i])
                row00 = coords[0]
                column00 = coords[1]

                coords = square10.get_coordinates(odd[i])
                row11 = coords[0]
                column11 = coords[1]

                enc += square.get_char(row00, column11)
                enc += square.get_char(row11, column00)
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
        return self.__enc(alphabet, text, key, True)

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
        return self.__enc(alphabet, text, key, False)
