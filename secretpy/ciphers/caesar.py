#!/usr/bin/python
# -*- encoding: utf-8 -*-
import secretpy.alphabets as al
from .affine import Affine


class Caesar:
    """
    The Caesar Cipher (Shift, Additive)
    """

    __affine = Affine()

    def encrypt(self, text, key=3, alphabet=al.ENGLISH):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: encrypted text
        :rtype: string
        """
        new_key = (1, key)
        return self.__affine.encrypt(text, new_key, alphabet)

    def decrypt(self, text, key=3, alphabet=al.ENGLISH):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: decrypted text
        :rtype: string
        """
        new_key = (1, key)
        return self.__affine.decrypt(text, new_key, alphabet)
