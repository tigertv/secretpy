#!/usr/bin/python
# -*- encoding: utf-8 -*-

from __future__ import division
import math
from .polybius import Polybius


class ADFGX:
    """
    The ADFGX Cipher
    """
    __header = u"adfgx"
    __polybius = Polybius()
    __alphabet = [
        u"a", u"b", u"c", u"d", u"e",
        u"f", u"g", u"h", u"ij", u"k",
        u"l", u"m", u"n", u"o", u"p",
        u"q", u"r", u"s", u"t", u"u",
        u"v", u"w", u"x", u"y", u"z"
    ]

    def __dec(self, alphabet, key, text):
        keysize = len(key)
        size = len(text)
        rows = int(math.ceil(size/keysize))
        reminder = size % keysize
        keyword = list(key)
        indices = sorted(range(len(keyword)), key=lambda k: keyword[k])

        myarr = list(indices)
        lefti = 0
        righti = 0
        for key, value in enumerate(indices):
            righti = lefti
            righti += rows
            if reminder > 0 and value > reminder-1:
                righti -= 1
            myarr[value] = text[lefti:righti]
            lefti = righti

        column = 0
        row = 0
        res = ''
        for i in range(size):
            res += (myarr[column][row])
            column += 1
            if column == keysize:
                column = 0
                row += 1

        code = [str(self.__header.index(char)+1) for char in res]
        code = "".join(code)
        dec = self.__polybius.decrypt(code, alphabet=alphabet)
        return dec

    def __enc(self, alphabet, key, text):
        ans0 = self.__polybius.encrypt(text, alphabet=alphabet)
        ans = [self.__header[int(char)-1] for char in ans0]

        keyword = list(key)
        keysize = len(key)
        size = len(ans)
        indices = sorted(range(len(keyword)), key=lambda k: keyword[k])
        row = int(math.ceil(size/keysize))
        for i in range(row):
            p = ""
            for j in range(keysize):
                myi = i*keysize+j
                if myi < len(ans):
                    eee = ans[myi]
                    p += "".join(eee)

        ans2 = ""
        for s in indices:
            ind = s
            while ind < size:
                p = ans[ind]
                ans2 += p
                ind += keysize

        return ans2

    def encrypt(self, text, key, alphabet=None):
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
        alphabet = alphabet or self.__alphabet
        return self.__enc(alphabet, key, text)

    def decrypt(self, text, key, alphabet=None):
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
        alphabet = alphabet or self.__alphabet
        return self.__dec(alphabet, key, text)
