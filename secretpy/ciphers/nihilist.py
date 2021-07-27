#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .polybius import Polybius
from secretpy import alphabets as al


class Nihilist:
    """
    The Nihilist Cipher
    """

    __polybius = Polybius()

    def encrypt(self, text, key=None, alphabet=al.ENGLISH_SQUARE_IJ):
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
        code = self.__polybius.encrypt(text, alphabet=alphabet)
        enc = ""
        for i in range(0, len(code), 2):
            char = self.__polybius.encrypt(key[(i >> 1) % len(key)],
                                           alphabet=alphabet)
            enc += str(int(code[i:i + 2]) + int(char)) + " "
        return enc.rstrip()

    def decrypt(self, text, key=None, alphabet=al.ENGLISH_SQUARE_IJ):
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
        code = text.split(' ')
        code = list(map(int, code))
        dec = ""
        for i in range(0, len(code)):
            char = self.__polybius.encrypt(key[i % len(key)],
                                           alphabet=alphabet)
            pair = str(code[i] - int(char))
            dec += self.__polybius.decrypt(pair, alphabet=alphabet)
        return dec

    def get_crypt_alphabet(self):
        return al.DECIMAL + " "
