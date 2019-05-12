#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .polybius_square import PolybiusSquare


class Playfair:
    """
    The Playfair Cipher
    """

    def __dec_two_letters(self, a, b, square):
        cols = square.get_columns()
        rows = square.get_rows()

        coords = square.get_coordinates(a)
        arow = coords[0]
        acolumn = coords[1]

        coords = square.get_coordinates(b)
        brow = coords[0]
        bcolumn = coords[1]

        if arow == brow:
            a = square.get_char(arow, (acolumn - 1) % cols)
            b = square.get_char(brow, (bcolumn - 1) % cols)
        elif acolumn == bcolumn:
            arow -= 1
            if arow >= rows:
                arow = 0
            a = square.get_char(arow, acolumn)

            brow -= 1
            if brow >= rows:
                brow = 0
            b = square.get_char(brow, bcolumn)
        else:
            a = square.get_char(arow, bcolumn)
            b = square.get_char(brow, acolumn)
        return a + b

    def __enc_two_letters(self, a, b, square):
        cols = square.get_columns()
        rows = square.get_rows()

        coords = square.get_coordinates(a)
        arow = coords[0]
        acolumn = coords[1]

        coords = square.get_coordinates(b)
        brow = coords[0]
        bcolumn = coords[1]

        if arow == brow:
            a = square.get_char(arow, (acolumn + 1) % cols)
            b = square.get_char(brow, (bcolumn + 1) % cols)
        elif acolumn == bcolumn:
            arow += 1
            if arow >= rows:
                arow = 0
            a = square.get_char(arow, acolumn)
            brow += 1
            if brow >= rows:
                brow = 0
            b = square.get_char(brow, bcolumn)
        else:
            a = square.get_char(arow, bcolumn)
            b = square.get_char(brow, acolumn)
        return a + b

    def __enc(self, alphabet, text, key):
        enc = u""
        insert_char = 'x'
        i = 1
        square = PolybiusSquare(alphabet, key)

        while i < len(text):
            if text[i-1] == text[i]:
                text = text[:i] + insert_char + text[i:]
            enc += self.__enc_two_letters(text[i-1], text[i], square)
            i += 2

        if len(text) & 1:
            enc += self.__enc_two_letters(text[-1], insert_char, square)

        return enc

    def __dec(self, alphabet, text, key):
        dec = ""
        insert_char = 'x'

        square = PolybiusSquare(alphabet, key)

        for i in range(1, len(text), 2):
            pair = self.__dec_two_letters(text[i-1], text[i], square)
            if len(dec) > 1 and dec[-1] == insert_char and pair[0] == dec[-2]:
                dec = dec[:-1] + pair[0]
                dec += pair[1]
            else:
                dec += self.__dec_two_letters(text[i-1], text[i], square)
        if dec[-1] == insert_char:
            dec = dec[:-1]
        return dec

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
        alphabet = alphabet or [
            u"a", u"b", u"c", u"d", u"e",
            u"f", u"g", u"h", u"ij", u"k",
            u"l", u"m", u"n", u"o", u"p",
            u"q", u"r", u"s", u"t", u"u",
            u"v", u"w", u"x", u"y", u"z"
        ]
        return self.__enc(alphabet, text, key)

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
        alphabet = alphabet or [
            u"a", u"b", u"c", u"d", u"e",
            u"f", u"g", u"h", u"ij", u"k",
            u"l", u"m", u"n", u"o", u"p",
            u"q", u"r", u"s", u"t", u"u",
            u"v", u"w", u"x", u"y", u"z"
        ]
        return self.__dec(alphabet, text, key)
