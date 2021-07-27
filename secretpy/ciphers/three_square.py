#!/usr/bin/python
# -*- encoding: utf-8 -*-
from secretpy import alphabets as al
from .polybius_square import PolybiusSquare
import random


class ThreeSquare:
    """
    The Three Square Cipher
    """

    def encrypt(self, text, key, alphabet=al.ENGLISH_SQUARE_IJ):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: tuple of 3 strings
        :type alphabet: string
        :return: text
        :rtype: string
        """
        square1 = PolybiusSquare(alphabet, key[0])
        square2 = PolybiusSquare(alphabet, key[1])
        square3 = PolybiusSquare(alphabet, key[2])

        res = []
        it = iter(text)
        rows = square1.get_rows()
        cols = square2.get_columns()
        while True:
            try:
                t = next(it)
            except StopIteration:
                break
            row1, column1 = square1.get_coordinates(t)
            try:
                t = next(it)
            except StopIteration:
                t = alphabet[-1][0]
            row2, column2 = square2.get_coordinates(t)

            i = random.randrange(rows)
            left = square1.get_char(i, column1)

            middle = square3.get_char(row1, column2)

            i = random.randrange(cols)
            right = square2.get_char(row2, i)

            res.append(left)
            res.append(middle)
            res.append(right)
        return u"".join(res)

    def decrypt(self, text, key, alphabet=al.ENGLISH_SQUARE_IJ):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: tuple of 3 strings
        :type alphabet: string
        :return: text
        :rtype: string
        """
        square1 = PolybiusSquare(alphabet, key[0])
        square2 = PolybiusSquare(alphabet, key[1])
        square3 = PolybiusSquare(alphabet, key[2])

        res = []
        it = iter(text)
        for t0, t1, t2 in zip(it, it, it):
            col1 = square1.get_coordinates(t0)[1]
            row3, col3 = square3.get_coordinates(t1)
            row2 = square2.get_coordinates(t2)[0]
            res.append(square1.get_char(row3, col1))
            res.append(square2.get_char(row2, col3))
        return u"".join(res)
