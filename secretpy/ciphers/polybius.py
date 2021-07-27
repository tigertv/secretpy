#!/usr/bin/python
# -*- encoding: utf-8 -*-
from itertools import starmap
from .polybius_square import PolybiusSquare
import secretpy.alphabets as al


class Polybius:
    """
    The Polybius Cipher
    """

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
        square = PolybiusSquare(alphabet, key)
        res = []
        for row, column in map(square.get_coordinates, text):
            res.append(str(row + 1))
            res.append(str(column + 1))
        return "".join(res)

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
        square = PolybiusSquare(alphabet, key)
        it = iter(map(lambda t: int(t) - 1, text))
        return "".join(starmap(square.get_char, zip(it, it)))

    def get_crypt_alphabet(self):
        return al.DECIMAL
