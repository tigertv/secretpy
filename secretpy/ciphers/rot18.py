#!/usr/bin/python

from .rot13 import Rot13
import secretpy.alphabet as al


class Rot18:
    """
    The Rot18 Cipher
    """
    __rot13 = Rot13()

    def __createAlphabet(self, alphabet):
        ahalf = len(alphabet) >> 1
        dhalf = len(al.DECIMAL) >> 1
        return (
            alphabet[:ahalf] + al.DECIMAL[:dhalf] +
            alphabet[ahalf:] + al.DECIMAL[dhalf:]
        )

    def __encDec(self, text, alphabet=None):
        alphabet = alphabet or al.ENGLISH
        alphabet = self.__createAlphabet(alphabet)
        return self.__rot13.encrypt(text, alphabet=alphabet)

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
        return self.__encDec(text, alphabet)

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
        return self.__encDec(text, alphabet)
