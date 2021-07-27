#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .polybius_square import PolybiusSquare
from .columnar_transposition import ColumnarTransposition
from secretpy import alphabets as al
from itertools import starmap


class ADFGVX:
    """
    The ADFGVX Cipher
    """
    __header = u"adfgvx"
    __columnar = ColumnarTransposition()
    __alphabet = (
        u"a", u"b", u"c", u"d", u"e", u"f",
        u"g", u"h", u"i", u"j", u"k", u"l",
        u"m", u"n", u"o", u"p", u"q", u"r",
        u"s", u"t", u"u", u"v", u"w", u"x",
        u"y", u"z", u"1", u"2", u"3", u"4",
        u"5", u"6", u"7", u"8", u"9", u"0",
    )

    def encrypt(self, text, key, alphabet=None):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English with numbers is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        alphabet = alphabet or self.__alphabet
        square = PolybiusSquare(alphabet)
        res = []
        for i, j in map(square.get_coordinates, text):
            res.append(self.__header[i])
            res.append(self.__header[j])

        res = "".join(res)
        # keyword is in english, alphabet is ENGLISH
        return self.__columnar.encrypt(res, key, al.ENGLISH)

    def decrypt(self, text, key, alphabet=None):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        alphabet = alphabet or self.__alphabet
        # keyword is in english, alphabet is ENGLISH
        res = self.__columnar.decrypt(text, key, al.ENGLISH)
        code = []
        it = iter(res)
        try:
            for i, j in zip(it, it):
                char = i
                ii = self.__header.index(char)
                char = j
                jj = self.__header.index(char)
                coord = (ii, jj)
                code.append(coord)
        except ValueError:
            wrchar = char.encode('utf-8')
            raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")

        square = PolybiusSquare(alphabet)
        return "".join(starmap(square.get_char, code))

    def get_crypt_alphabet(self):
        return self.__header
