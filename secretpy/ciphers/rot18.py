#!/usr/bin/python

from .rot13 import Rot13
import secretpy.alphabets as al


class Rot18:
    """
    The Rot18 Cipher
    """
    __rot13 = Rot13()

    def __init__(self):
        alphabet = al.ENGLISH
        half = len(alphabet) >> 1
        self.__alphabet = alphabet[:half] + al.DECIMAL[:5] + alphabet[half:] + al.DECIMAL[5:]

    def __crypt(self, text, alphabet):
        return self.__rot13.encrypt(text, alphabet=self.__alphabet)

    def encrypt(self, text, key=None, alphabet=None):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: is not used
        :param alphabet: is not used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return self.__crypt(text, self.__alphabet)

    def decrypt(self, text, key=None, alphabet=None):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: is not used
        :param alphabet: is not used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return self.__crypt(text, self.__alphabet)

    def get_fixed_alphabet(self):
        return self.__alphabet
