#!/usr/bin/python

from .rot13 import Rot13


class Rot47:
    """
    The Rot47 Cipher
    """

    __rot13 = Rot13()

    def __init__(self):
        self.__alphabet = "".join([chr(asc) for asc in range(33, 33 + 47*2)])

    def __encDec(self, text):
        return self.__rot13.encrypt(text, alphabet=self.__alphabet)

    def encrypt(self, text, key=None, alphabet=None):
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
        return self.__encDec(text)

    def decrypt(self, text, key=None, alphabet=None):
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
        return self.__encDec(text)
