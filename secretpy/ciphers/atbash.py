#!/usr/bin/python
from secretpy import alphabets as al
from .affine import Affine


class Atbash:
    """
    The Atbash Cipher
    """

    __affine = Affine()

    def encrypt(self, text, key=None, alphabet=al.ENGLISH):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: is not used
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string or tuple of strings
        :return: text
        :rtype: string
        """
        new_key = (-1, -1)
        return self.__affine.encrypt(text, new_key, alphabet)

    def decrypt(self, text, key=None, alphabet=al.ENGLISH):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: is not used
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string or tuple of strings
        :return: text
        :rtype: string
        """
        new_key = (-1, -1)
        return self.__affine.decrypt(text, new_key, alphabet)
