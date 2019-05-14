#!/usr/bin/python
# -*- encoding: utf-8 -*-
from secretpy import alphabets


class ColumnarTransposition:
    """
    The Columnar Transposition Cipher
    """

    def __dec(self, alphabet, key, text):
        # add endings to the text to fill the square
        chars = [alphabets.get_index_in_alphabet(char, alphabet)
                 for char in key]
        keyorder = sorted(enumerate(chars), key=lambda x: x[1])
        ret = u""
        rows = int(len(text) / len(key))
        cols = [(text[i * rows: (i + 1) * rows], keyorder[i][0])
                for i in range(len(key))]
        cols2 = sorted(cols, key=lambda x: x[1])
        for j in range(rows):
            for i in range(len(cols2)):
                ret += cols2[i][0][j]
        return ret

    def __enc(self, alphabet, key, text):
        # add endings to the text to fill the square
        rmd = len(text) % len(key)
        if rmd != 0:
            text += alphabet[-1] * (len(key) - rmd)

        chars = [alphabets.get_index_in_alphabet(char, alphabet)
                 for char in key]
        keyorder1 = sorted(enumerate(chars), key=lambda x: x[1])

        ret = u""
        for i in range(len(key)):
            ret += text[keyorder1[i][0]::len(key)]

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
