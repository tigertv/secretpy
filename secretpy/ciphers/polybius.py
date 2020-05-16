#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .polybius_square import PolybiusSquare


class Polybius:
    """
    The Polybius Cipher
    """

    def __encDec(self, alphabet, text, key, isEncrypt=True):
        square = PolybiusSquare(alphabet, key)
        res = ""
        header = range(1, square.get_columns() + 1)
        header = "".join(map(str, header))
        if isEncrypt:
            for char in text:
                coords = square.get_coordinates(char)
                row = coords[0]
                column = coords[1]
                res += header[row] + header[column]
        else:
            for i in range(0, len(text), 2):
                try:
                    row = header.index(text[i])
                except ValueError as e:
                    wrchar = text[i].encode('utf-8')
                    raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
                try:
                    column = header.index(text[i+1])
                except ValueError as e:
                    wrchar = text[i+1].encode('utf-8')
                    raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
                res += square.get_char(row, column)
        return res

    def encrypt(self, text, key="", alphabet=None):
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
        alphabet = alphabet or (
            u"a", u"b", u"c", u"d", u"e",
            u"f", u"g", u"h", u"ij", u"k",
            u"l", u"m", u"n", u"o", u"p",
            u"q", u"r", u"s", u"t", u"u",
            u"v", u"w", u"x", u"y", u"z"
        )
        return self.__encDec(alphabet, text, key, True)

    def decrypt(self, text, key="", alphabet=None):
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
        alphabet = alphabet or (
            u"a", u"b", u"c", u"d", u"e",
            u"f", u"g", u"h", u"ij", u"k",
            u"l", u"m", u"n", u"o", u"p",
            u"q", u"r", u"s", u"t", u"u",
            u"v", u"w", u"x", u"y", u"z"
        )
        return self.__encDec(alphabet, text, key, False)
