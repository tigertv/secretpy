#!/usr/bin/python
# -*- encoding: utf-8 -*-

import math
from collections import OrderedDict


class FourSquare:
    """
    The Four-Square Cipher
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

    def __enc(self, alphabet, text, key, isEncrypt):
        side = int(math.ceil(math.sqrt(len(alphabet))))
        alphabet01 = self.__create_alphabet_by_key(alphabet, key[0])
        alphabet10 = self.__create_alphabet_by_key(alphabet, key[1])

        # text encryption
        if len(text) % 2:
            text += alphabet[-1][0]
        odd = text[1::2]
        even = text[::2]
        enc = u""
        if isEncrypt:
            for i in range(len(even)):
                index00 = self.__find_index_in_alphabet(even[i], alphabet)
                row00 = int(index00 / side)
                column00 = index00 % side

                index11 = self.__find_index_in_alphabet(odd[i], alphabet)
                row11 = int(index11 / side)
                column11 = index11 % side

                enc += alphabet01[row00 * side + column11][0]
                enc += alphabet10[row11 * side + column00][0]
        else:
            for i in range(len(even)):
                index00 = self.__find_index_in_alphabet(even[i], alphabet01)
                row00 = int(index00 / side)
                column00 = index00 % side

                index11 = self.__find_index_in_alphabet(odd[i], alphabet10)
                row11 = int(index11 / side)
                column11 = index11 % side

                enc += alphabet[row00 * side + column11][0]
                enc += alphabet[row11 * side + column00][0]
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
        return self.__enc(alphabet, text, key, True)

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
        return self.__enc(alphabet, text, key, False)
