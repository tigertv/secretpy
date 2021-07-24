#!/usr/bin/python
# -*- encoding: utf-8 -*-
from secretpy import alphabets as al
from itertools import chain


class Autokey:
    """
    The Autokey Cipher
    """

    def __crypt(self, alphabet, key, text, is_encrypt):
        indexes = {c: i for i, letters in enumerate(alphabet) for c in letters}
        res = []

        if is_encrypt == 1:
            new_key = chain(key, text)
        else:
            new_key = chain(key, res)

        for t in text:
            k = next(new_key)
            try:
                i = indexes[t]
            except ValueError:
                wrchar = t.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            try:
                i += is_encrypt * indexes[k]
            except ValueError:
                wrchar = k.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            i = i % len(alphabet)
            res.append(alphabet[i][0])
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
        :type alphabet: string or tuple of strings
        :return: text
        :rtype: string
        """
        return self.__crypt(alphabet, key, text, 1)

    def decrypt(self, text, key, alphabet=al.ENGLISH):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: string
        :type alphabet: string or tuple of strings
        :return: text
        :rtype: string
        """
        return self.__crypt(alphabet, key, text, -1)
