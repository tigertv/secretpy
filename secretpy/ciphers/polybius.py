#!/usr/bin/python
# -*- encoding: utf-8 -*-

import secretpy.alphabets as al
from .polybius_square import PolybiusSquare


class Polybius:
    """
    The Polybius Cipher
    """

    def encrypt(self, text, key="", alphabet=al.ENGLISH_SQUARE_IJ):
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
        square = PolybiusSquare(alphabet, key)
        header = list(map(str, range(1, square.get_columns() + 1)))
        res = []
        for t in text:
            row, column = square.get_coordinates(t)
            res.append(header[row])
            res.append(header[column])
        return "".join(res)

    def decrypt(self, text, key="", alphabet=al.ENGLISH_SQUARE_IJ):
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
        square = PolybiusSquare(alphabet, key)
        header = list(map(str, range(1, square.get_columns() + 1)))
        res = []
        for i in range(1, len(text), 2):
            try:
                row = header.index(text[i - 1])
            except ValueError:
                wrchar = text[i - 1].encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            try:
                column = header.index(text[i])
            except ValueError:
                wrchar = text[i].encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            res.append(square.get_char(row, column))
        return "".join(res)

    def get_crypt_alphabet(self):
        return al.DECIMAL
