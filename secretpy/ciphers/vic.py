#!/usr/bin/python
# -*- encoding: utf-8 -*-
from secretpy import alphabets as al
from itertools import cycle


class Vic:
    """
    The Vic Cipher
    """

    def __crypt(self, alphabet, text, key):
        columns = []
        subst = {}
        width = 10
        # prepare substitution from alphabet
        for i, value in enumerate(alphabet):
            if value == "":
                columns.append(i)
            elif i < width:
                subst[value] = (i,)
            else:
                row, col = divmod(i, width)
                subst[value] = (columns[row - 1], col)

        # encode chars to numbers
        code = []
        for t in text:
            code.extend(subst[t])

        res = []
        row = 0
        for c, k in zip(code, cycle(key)):
            # apply the key
            i = (c + k) % width
            # encode numbers to chars
            if row == 0 and (i in columns):
                row = columns.index(i) + 1
            else:
                res.append(alphabet[row * width + i][0])
                row = 0
        return u"".join(res)

    def encrypt(self, text, key=None, alphabet=al.ENGLISH_SQUARE_IJ):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: number string
        :type alphabet: string
        :return: text
        :rtype: string
        """
        # prepare key
        new_key = (int(i) for i in key)
        return self.__crypt(alphabet, text, new_key)

    def decrypt(self, text, key=None, alphabet=al.ENGLISH_SQUARE_IJ):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: number string
        :type alphabet: string
        :return: text
        :rtype: string
        """
        width = 10
        # invert key
        new_key = (width - int(i) for i in key)
        return self.__crypt(alphabet, text, new_key)
