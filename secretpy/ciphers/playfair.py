#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .polybius_square import PolybiusSquare
from secretpy import alphabets as al


class Playfair:
    """
    The Playfair Cipher
    """

    # encrypt or decrypt two letters
    def __crypt(self, a, b, square, is_encrypt):
        cols = square.get_columns()
        rows = square.get_rows()

        arow, acolumn = square.get_coordinates(a)
        brow, bcolumn = square.get_coordinates(b)

        if arow == brow:
            acolumn = (acolumn + is_encrypt) % cols
            bcolumn = (bcolumn + is_encrypt) % cols
        elif acolumn == bcolumn:
            arow += is_encrypt
            brow += is_encrypt
            if arow >= rows:
                arow = 0
            if brow >= rows:
                brow = 0
        else:
            acolumn, bcolumn = bcolumn, acolumn
        a = square.get_char(arow, acolumn)
        b = square.get_char(brow, bcolumn)
        return a + b

    def encrypt(self, text, key="", alphabet=al.ENGLISH_SQUARE_IJ):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, ENGLISH_SQUARE_IJ is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        insert_char = 'x'
        square = PolybiusSquare(alphabet, key)

        # prepare text
        txt = []
        i = 1
        while i < len(text):
            txt.append(text[i - 1])
            if text[i - 1] == text[i]:
                txt.append(insert_char)
                i += 1
            else:
                txt.append(text[i])
                i += 2
        # add the last character
        if i == len(text):
            txt.append(text[i - 1])
            txt.append(insert_char)

        return "".join(self.__crypt(txt[i - 1], txt[i], square, 1) for i in range(1, len(txt), 2))

    def decrypt(self, text, key="", alphabet=al.ENGLISH_SQUARE_IJ):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, ENGLISH_SQUARE_IJ is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        insert_char = 'x'
        square = PolybiusSquare(alphabet, key)

        res = [self.__crypt(text[i - 1], text[i], square, -1) for i in range(1, len(text), 2)]
        # remove the insert character
        for i in range(1, len(res)):
            if res[i - 1][0] == res[i][0] and res[i - 1][1] == insert_char:
                res[i - 1] = res[i - 1][0]
        # check the last character
        if res[-1][1] == insert_char:
            res[-1] = res[-1][0]

        return "".join(res)
