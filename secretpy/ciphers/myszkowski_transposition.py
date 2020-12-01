#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import alphabets


class MyszkowskiTransposition:
    """
    The Myszkowski Transposition Cipher
    """
    def __keycols(self, key, alphabet):
        chars = [alphabets.get_index_in_alphabet(char, alphabet) for char in key]
        chars = sorted(enumerate(chars), key=lambda x: x[1])
        cols = [[chars[0][0]]]

        for i in range(1, len(key)):
            if chars[i-1][1] == chars[i][1]:
                cols[-1].append(chars[i][0])
            else:
                cols.append([chars[i][0]])
        return cols

    def __enc(self, alphabet, key, text):
        ret = u""
        cols = self.__keycols(key, alphabet)
        lines = len(text) // len(key)
        if len(text) % len(key):
            lines += 1

        for col in cols:
            for a in range(lines):
                for i in col:
                    if i < len(text):
                        ret += text[i]
                col = list(map(lambda x: x + len(key), col))
        return ret

    def __dec(self, alphabet, key, text):
        ret = u""
        cols = self.__keycols(key, alphabet)

        lines = len(text) // len(key)
        if len(text) % len(key):
            lines += 1

        m = [""] * len(key)
        ci = 0
        for col in cols:
            ccol = col
            for line in range(lines):
                for i, value in enumerate(ccol):
                    if value < len(text):
                        m[col[i]] += text[ci]
                        ci += 1
                ccol = list(map(lambda x: x + len(key), ccol))

        for i in range(lines):
            for j in m:
                try:
                    ret += j[i]
                except IndexError:
                    pass
        return ret

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
        alphabet = alphabet or alphabets.ENGLISH
        return self.__enc(alphabet, key, text)

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
        alphabet = alphabet or alphabets.ENGLISH
        return self.__dec(alphabet, key, text)
