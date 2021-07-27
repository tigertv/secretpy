#!/usr/bin/python
# -*- encoding: utf-8 -*-
from itertools import cycle


class Spiral:
    """
    The Spiral Transposition Cipher

    It's a variant of the Route Cipher
    Spiral inwards, clockwise, starting at the top right.

    https://en.wikipedia.org/wiki/Transposition_cipher#Route_cipher
    """
    def __crypt(self, text, key, is_encrypt):
        columns, rmd = divmod(len(text), key)

        # init
        top = 0
        left = key - 1
        bottom = key * (columns + (rmd > 0)) - 1

        if rmd:
            right = len(text) - rmd
        else:
            right = len(text) - key
        i = right
        right -= key

        if is_encrypt:
            res = []
        else:
            ti = 0
            res = [None] * len(text)

        # i = from, j = to

        # top right to bottom right
        j = bottom
        if i == j:
            if is_encrypt:
                res.append(text[i])
            else:
                res[i] = text[ti]
            return u"".join(res)
        temp = j
        if temp > len(text):
            temp = len(text)
        for p in range(i, temp):
            if is_encrypt:
                res.append(text[p])
            else:
                res[p] = text[ti]
                ti += 1
        # change limit
        bottom -= 1 + key

        # bottom right to bottom left
        i = j
        if rmd:  # additional condition
            i -= key
        if i < 0:  # additional condition
            return u"".join(res)
        j = left
        if i == j and rmd == 0:
            if is_encrypt:
                res.append(text[i])
            else:
                res[i] = text[ti]
            return u"".join(res)
        for p in range(i, j, -key):
            if is_encrypt:
                res.append(text[p])
            else:
                res[p] = text[ti]
                ti += 1
        # change limit
        left += key - 1

        # ([limit, change_limit, delta], ...)
        steps = ([top, key + 1, -1], [right, 1 - key, key], [bottom, -key - 1, 1], [left, key - 1, -key])

        # bottom left to top left
        # top left to top right
        # top right to bottom right
        # bottom right to bottom left
        for step in cycle(steps):
            i = j
            j = step[0]
            step[0] += step[1]
            if i == j:
                if is_encrypt:
                    res.append(text[i])
                else:
                    res[i] = text[ti]
                break
            for p in range(i, j, step[2]):
                if is_encrypt:
                    res.append(text[p])
                else:
                    res[p] = text[ti]
                    ti += 1
        return u"".join(res)

    def encrypt(self, text, key, alphabet=None):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Number of rows
        :param alphabet: Alphabet is not used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return self.__crypt(text, key, True)

    def decrypt(self, text, key, alphabet=None):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Number of rows
        :param alphabet: Alphabet is not used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return self.__crypt(text, key, False)
