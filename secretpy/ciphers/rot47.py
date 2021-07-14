#!/usr/bin/python

from .caesar import Caesar


class Rot47:
    """
    The Rot47 Cipher
    """

    __caesar = Caesar()
    __alphabet = "".join(chr(asc) for asc in range(33, 33 + 47 * 2))

    def __crypt(self, text):
        return self.__caesar.encrypt(text, 47, self.__alphabet)

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
        return self.__crypt(text)

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
        return self.__crypt(text)

    def get_fixed_alphabet(self):
        return self.__alphabet
