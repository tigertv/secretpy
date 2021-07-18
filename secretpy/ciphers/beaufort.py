#!/usr/bin/python
# -*- encoding: utf-8 -*-

from itertools import cycle
from secretpy import alphabets as al


class Beaufort:
    """
    The Beaufort Cipher
    """

    def __crypt(self, alphabet, key, text):
        # prepare alphabet for substitution
        indexes = {c: i for i, letters in enumerate(alphabet) for c in letters}
        # prepare key
        key_indexes = (indexes[c] for c in key)
        res = []
        for k, t in zip(cycle(key_indexes), text):
            try:
                i = k - indexes[t]
                res.append(alphabet[i][0])
            except KeyError:
                wrchar = t.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
        return "".join(res)

    def encrypt(self, text, key, alphabet=al.ENGLISH):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: string
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return self.__crypt(alphabet, key, text)

    def decrypt(self, text, key, alphabet=al.ENGLISH):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: string
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return self.__crypt(alphabet, key, text)
