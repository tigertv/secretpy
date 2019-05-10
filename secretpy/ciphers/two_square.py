#!/usr/bin/python
# -*- encoding: utf-8 -*-

import math
from collections import OrderedDict


class TwoSquare:
    """
    The Two-Square Cipher
    """

    def __find_index_in_alphabet(self, char, alphabet):
        for j in range(len(alphabet)):
            try:
                alphabet[j].index(char)
                break
            except ValueError:
                pass
        return j

    def __create_alphabet_by_key(self, alphabet, key):
        keyi = []
        for char in key:
            index = self.__find_index_in_alphabet(char, alphabet)
            keyi.append(index)

        # remove dublicates
        keyi = OrderedDict.fromkeys(keyi)
        alph_out = []
        for i in keyi:
            alph_out.append(alphabet[i])

        for i in range(len(alphabet)):
            if i not in keyi:
                alph_out.append(alphabet[i])

        return alph_out

    def __enc(self, alphabet, text, key):
        side = int(math.ceil(math.sqrt(len(alphabet))))
        alphabet1 = self.__create_alphabet_by_key(alphabet, key[0])
        alphabet2 = self.__create_alphabet_by_key(alphabet, key[1])

        # text encryption
        if len(text) % 2:
            text += alphabet[-1][0]
        odd = text[1::2]
        even = text[::2]
        enc = u""

        for i in range(len(even)):
            index1 = self.__find_index_in_alphabet(even[i], alphabet1)
            row1 = int(index1 / side)
            column1 = index1 % side

            index2 = self.__find_index_in_alphabet(odd[i], alphabet2)
            row2 = int(index2 / side)
            column2 = index2 % side

            if column1 == column2:
                enc += alphabet1[row2 * side + column1][0]
                enc += alphabet2[row1 * side + column1][0]
            else:
                enc += alphabet1[row1 * side + column2][0]
                enc += alphabet2[row2 * side + column1][0]
        return enc

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
        return self.__enc(alphabet, text, key)

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
        return self.__enc(alphabet, text, key)
