#!/usr/bin/python
# -*- encoding: utf-8 -*-
from secretpy import alphabets


class ColumnarTransposition:
    """
    The Columnar Transposition Cipher
    """

    def __dec(self, alphabet, key, text):
        chars = [alphabets.get_index_in_alphabet(char, alphabet)
                 for char in key]
        keyorder = sorted(enumerate(chars), key=lambda x: x[1])
        rows = int(len(text) / len(key))
        roworder = [0] * len(key)
        for i, (j, _) in enumerate(keyorder):
            roworder[j] = i * rows
        return u"".join(text[i+j] for j in range(rows) for i in roworder)

    def __enc(self, alphabet, key, text):
        # add endings to the text to fill the square
        rmd = len(text) % len(key)
        if rmd != 0:
            text += alphabet[-1] * (len(key) - rmd)

        chars = [alphabets.get_index_in_alphabet(char, alphabet)
                 for char in key]
        keyorder = sorted(enumerate(chars), key=lambda x: x[1])
        return u"".join(text[i::len(key)] for i, _ in keyorder)

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
