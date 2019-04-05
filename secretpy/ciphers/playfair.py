#!/usr/bin/python
# -*- encoding: utf-8 -*-

import math


class Playfair:
    """
    The Playfair Cipher
    """

    def __find_index_in_alphabet(self, char, alphabet):
        for j in range(len(alphabet)):
            try:
                alphabet[j].index(char)
                break
            except ValueError:
                pass
        return j

    def __dec_two_letters(self, a, b, alphabet):
        side = int(math.ceil(math.sqrt(len(alphabet))))

        ia = self.__find_index_in_alphabet(a, alphabet)
        arow = int(ia / side)
        acolumn = ia % side

        ib = self.__find_index_in_alphabet(b, alphabet)
        brow = int(ib / side)
        bcolumn = ib % side

        if arow == brow:
            a = alphabet[arow * side + (acolumn - 1) % side][0]
            b = alphabet[brow * side + (bcolumn - 1) % side][0]
        elif acolumn == bcolumn:
            i = (arow - 1) * side + acolumn
            if i >= len(alphabet):
                i = acolumn
            a = alphabet[i][0]
            i = (brow - 1) * side + bcolumn
            if i >= len(alphabet):
                i = bcolumn
            b = alphabet[i][0]
        else:
            a = alphabet[arow * 5 + bcolumn][0]
            b = alphabet[brow * 5 + acolumn][0]
        return a + b

    def __enc_two_letters(self, a, b, alphabet):
        side = int(math.ceil(math.sqrt(len(alphabet))))

        ia = self.__find_index_in_alphabet(a, alphabet)
        arow = int(ia / side)
        acolumn = ia % side

        ib = self.__find_index_in_alphabet(b, alphabet)
        brow = int(ib / side)
        bcolumn = ib % side

        if arow == brow:
            a = alphabet[arow * side + (acolumn + 1) % side][0]
            b = alphabet[brow * side + (bcolumn + 1) % side][0]
        elif acolumn == bcolumn:
            i = (arow + 1) * side + acolumn
            if i >= len(alphabet):
                i = acolumn
            a = alphabet[i][0]
            i = (brow + 1) * side + bcolumn
            if i >= len(alphabet):
                i = bcolumn
            b = alphabet[i][0]
        else:
            a = alphabet[arow * side + bcolumn][0]
            b = alphabet[brow * side + acolumn][0]
        return a + b

    def __enc(self, alphabet, text):
        enc = u""
        insert_char = 'x'
        i = 1

        while i < len(text):
            if text[i-1] == text[i]:
                text = text[:i] + insert_char + text[i:]
            enc += self.__enc_two_letters(text[i-1], text[i], alphabet)
            i += 2

        if len(text) & 1:
            enc += self.__enc_two_letters(text[-1], insert_char, alphabet)

        return enc

    def __dec(self, alphabet, text):
        dec = ""
        insert_char = 'x'

        for i in range(1, len(text), 2):
            pair = self.__dec_two_letters(text[i-1], text[i], alphabet)
            if len(dec) > 1 and dec[-1] == insert_char and pair[0] == dec[-2]:
                dec = dec[:-1] + pair[0]
                dec += pair[1]
            else:
                dec += self.__dec_two_letters(text[i-1], text[i], alphabet)
        if dec[-1] == insert_char:
            dec = dec[:-1]
        return dec

    def encrypt(self, text, key=None, alphabet=None):
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
        return self.__enc(alphabet, text)

    def decrypt(self, text, key=None, alphabet=None):
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
        return self.__dec(alphabet, text)
