#!/usr/bin/python

from .rot13 import Rot13
import secretpy.alphabets as al


class Rot18:
    """
    The Rot18 Cipher
    """
    __rot13 = Rot13()

    def __create_alphabet(self, alphabet):
        ahalf = len(alphabet) >> 1
        return (
            alphabet[:ahalf] + al.DECIMAL[:5] +
            alphabet[ahalf:] + al.DECIMAL[5:]
        )

    def __crypt(self, text, alphabet=None):
        alphabet = alphabet or al.ENGLISH
        alphabet = self.__create_alphabet(alphabet)
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
        return self.__crypt(text, alphabet)

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
        return self.__crypt(text, alphabet)
