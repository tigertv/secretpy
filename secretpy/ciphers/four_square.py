#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .polybius_square import PolybiusSquare
from secretpy import alphabets as al


class FourSquare:
    """
    The Four-Square Cipher
    """

    def __crypt(self, alphabet, text, key, is_encrypt):
        square01 = PolybiusSquare(alphabet, key[0])
        square10 = PolybiusSquare(alphabet, key[1])
        square = PolybiusSquare(alphabet)
        square00 = square
        square11 = square

        res = []
        if is_encrypt:
            square01, square10, square00, square11 = square00, square11, square01, square10

        # text encryption
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
            row00, column00 = square01.get_coordinates(even)
            row11, column11 = square10.get_coordinates(odd)
            res.append(square00.get_char(row00, column11))
            res.append(square11.get_char(row11, column00))
        return "".join(res)

    def encrypt(self, text, key=None, alphabet=al.ENGLISH_SQUARE_IJ):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: tuple of two strings
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return self.__crypt(alphabet, text, key, True)

    def decrypt(self, text, key=None, alphabet=al.ENGLISH_SQUARE_IJ):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: tuple of two strings
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return self.__crypt(alphabet, text, key, False)
