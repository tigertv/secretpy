#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .polybius import Polybius


class Nihilist:
    """
    The Nihilist Cipher
    """

    __polybius = Polybius()

    def __enc(self, alphabet, text, key):
        code = self.__polybius.encrypt(text, alphabet=alphabet)
        enc = ""
        for i in range(0, len(code), 2):
            char = self.__polybius.encrypt(key[(i >> 1) % len(key)],
                                           alphabet=alphabet)
            enc += str(int(code[i:i+2]) + int(char)) + " "
        return enc.rstrip()

    def __dec(self, alphabet, text, key):
        code = text.split(' ')
        code = list(map(int, code))
        dec = ""
        for i in range(0, len(code)):
            char = self.__polybius.encrypt(key[i % len(key)],
                                           alphabet=alphabet)
            pair = str(code[i] - int(char))
            dec += self.__polybius.decrypt(pair, alphabet=alphabet)
        return dec

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
        alphabet = alphabet or [
            u"a", u"b", u"c", u"d", u"e",
            u"f", u"g", u"h", u"ij", u"k",
            u"l", u"m", u"n", u"o", u"p",
            u"q", u"r", u"s", u"t", u"u",
            u"v", u"w", u"x", u"y", u"z"
        ]
        return self.__enc(alphabet, text, key)

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
        alphabet = alphabet or [
            u"a", u"b", u"c", u"d", u"e",
            u"f", u"g", u"h", u'ij', u"k",
            u"l", u"m", u"n", u"o", u"p",
            u"q", u"r", u"s", u"t", u"u",
            u"v", u"w", u"x", u"y", u"z"
        ]
        return self.__dec(alphabet, text, key)
