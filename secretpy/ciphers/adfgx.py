#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .polybius_square import PolybiusSquare
from .columnar_transposition import ColumnarTransposition
from secretpy import alphabets as al
from itertools import starmap


class ADFGX:
    """
    The ADFGX Cipher
    """
    __header = u"adfgx"
    __columnar = ColumnarTransposition()

    def encrypt(self, text, key, alphabet=al.ENGLISH_SQUARE_IJ):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key is in ENGLISH
        :param alphabet: Alphabet which will be used(length=25),
                         if there is no a value, ENGLISH_SQUARE_IJ is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        square = PolybiusSquare(alphabet)
        res = []
        for i, j in map(square.get_coordinates, text):
            res.append(self.__header[i])
            res.append(self.__header[j])

        res = "".join(res)
        # keyword is in english, alphabet is ENGLISH
        return self.__columnar.encrypt(res, key, al.ENGLISH)

    def decrypt(self, text, key, alphabet=al.ENGLISH_SQUARE_IJ):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key is in ENGLISH
        :param alphabet: Alphabet which will be used(length=25),
                         if there is no a value, ENGLISH_SQUARE_IJ is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
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
