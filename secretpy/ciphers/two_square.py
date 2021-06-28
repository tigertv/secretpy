#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .polybius_square import PolybiusSquare
from secretpy import alphabets as al


class TwoSquare:
    """
    The Two-Square Cipher, also called Double Playfair
    """

    def __crypt(self, alphabet, text, key):
        square1 = PolybiusSquare(alphabet, key[0])
        square2 = PolybiusSquare(alphabet, key[1])

        # text encryption
        res = []
        it = iter(text)
        while True:
            try:
                even = next(it)
            except StopIteration:
                break
            try:
                odd = next(it)
            except StopIteration:
                # add the last letter in the alphabet
                odd = alphabet[-1][0]
            row1, column1 = square1.get_coordinates(even)
            row2, column2 = square2.get_coordinates(odd)

            if column1 == column2:
                row1, row2 = row2, row1

            res.append(square1.get_char(row1, column2))
            res.append(square2.get_char(row2, column1))

        return "".join(res)

    def encrypt(self, text, key=None, alphabet=al.ENGLISH_SQUARE_IJ):
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
        return self.__crypt(alphabet, text, key)

    def decrypt(self, text, key=None, alphabet=al.ENGLISH_SQUARE_IJ):
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
        return self.__crypt(alphabet, text, key)
