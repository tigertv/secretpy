#!/usr/bin/python
# -*- encoding: utf-8 -*-
from secretpy import alphabets as al
from .gronsfeld import Gronsfeld


class Vigenere:
    """
    The Vigenere Cipher
    """
    __gronsfeld = Gronsfeld()

    def __crypt(self, alphabet, key):
        # prepare alphabet for substitution
        indexes = {c: i for i, letters in enumerate(alphabet) for c in letters}
        # prepare key
        return (indexes[c] for c in key)

    def encrypt(self, text, key, alphabet=al.ENGLISH):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: string
        :type alphabet: string
        :return: text
        :rtype: string
        """
        new_key = self.__crypt(alphabet, key)
        return self.__gronsfeld.encrypt(text, new_key, alphabet)

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
        new_key = self.__crypt(alphabet, key)
        return self.__gronsfeld.decrypt(text, new_key, alphabet)
