#!/usr/bin/python
# -*- encoding: utf-8 -*-

import math


class Polybius:
    """
    The Polybius Cipher
    """

    def __enc(self, alphabet, text):
        ans0 = ""
        size = int(math.ceil(math.sqrt(len(alphabet))))
        header = range(1, (size+1))
        header = "".join(map(str, header))
        for i in range(len(text)):
            char = text[i]
            for j in range(len(alphabet)):
                try:
                    alphabet[j].index(char)
                    break
                except ValueError:
                    pass
            row = int(j/size)
            column = j % size
            ans0 += header[row] + header[column]
        return ans0

    def __dec(self, alphabet, text):
        dec = ""
        size = len(text)
        side = int(math.ceil(math.sqrt(len(alphabet))))
        header = range(1, side + 1)
        header = "".join(map(str, header))
        for i in range(size >> 1):
            row = header.index(text[i*2])
            column = header.index(text[i*2+1])
            index = row*side + column
            dec += alphabet[index][0]
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
