#!/usr/bin/python
# -*- encoding: utf-8 -*-
from itertools import cycle
from secretpy import alphabets as al


class Gronsfeld:
    """
    The Gronsfeld Cipher
    """

    def __crypt(self, alphabet, key, text):
        # prepare alphabet for substitution
        indexes = {c: i for i, letters in enumerate(alphabet) for c in letters}
        # prepare key
        res = []
        for keyi, char in zip(cycle(key), text):
            try:
                i = indexes[char] - keyi
                res.append(alphabet[i][0])
            except KeyError:
                wrchar = char.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
        return "".join(res)

    def encrypt(self, text, key, alphabet=al.ENGLISH):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: tuple of integers
        :type alphabet: string
        :return: text
        :rtype: string
        """
        # sanitize and invert the key
        new_key = (-i % len(alphabet) for i in key)
        return self.__crypt(alphabet, new_key, text)

    def decrypt(self, text, key, alphabet=al.ENGLISH):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: tuple of integers
        :type alphabet: string
        :return: text
        :rtype: string
        """
        # sanitize the key
        new_key = (i % len(alphabet) for i in key)
        return self.__crypt(alphabet, new_key, text)
