#!/usr/bin/python
# -*- encoding: utf-8 -*-
from __future__ import division
import math
from .polybius import Polybius


class ADFGVX:
    """
    The ADFGVX Cipher
    """
    __header = u"adfgvx"
    __polybius = Polybius()
    __alphabet = [
        u"a", u"b", u"c", u"d", u"e", u"f",
        u"g", u"h", u"ij", u"k", u"l", u"m",
        u"n", u"o", u"p", u"q", u"r", u"s",
        u"t", u"u", u"v", u"w", u"x", u"y",
        u"z", u"1", u"2", u"3", u"4", u"5",
        u"6", u"7", u"8", u"9", u"0", u".",
    ]

    def encrypt(self, text, key, alphabet=None):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        alphabet = alphabet or self.__alphabet
        ans = self.__polybius.encrypt(text, alphabet=alphabet)
        ans = [self.__header[int(char) - 1] for char in ans]

        keysize = len(key)
        size = len(ans)
        indices = sorted(range(keysize), key=lambda k: key[k])
        return "".join(ans[ind] for s in indices for ind in range(s, size, keysize))

    def decrypt(self, text, key, alphabet=None):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        alphabet = alphabet or self.__alphabet
        keysize = len(key)
        size = len(text)
        rows = int(math.ceil(size / keysize))
        reminder = size % keysize
        indices = sorted(range(keysize), key=lambda k: key[k])

        myarr = [0] * keysize
        lefti = 0
        righti = 0
        for key, value in enumerate(indices):
            righti = lefti
            righti += rows
            if reminder > 0 and value > reminder - 1:
                righti -= 1
            myarr[value] = text[lefti:righti]
            lefti = righti

        column = 0
        row = 0
        res = []
        for i in range(size):
            res.append(myarr[column][row])
            column += 1
            if column == keysize:
                column = 0
                row += 1
        code = []
        try:
            for char in res:
                code.append(self.__header.index(char) + 1)
        except ValueError:
            wrchar = char.encode('utf-8')
            raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")

        code = "".join(map(str, code))
        return self.__polybius.decrypt(code, alphabet=alphabet)
