#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .polybius import Polybius


class Bifid:
    """
    The Bifid Cipher
    """

    __polybius = Polybius()

    def __enc(self, alphabet, text, key):
        code = self.__polybius.encrypt(text, alphabet=alphabet)
        even = code[::2]
        odd = code[1::2]
        ret = ""
        for i in range(0, len(even), key):
            ret += even[i:i+key] + odd[i:i+key]
        return self.__polybius.decrypt(ret, alphabet=alphabet)

    def __dec(self, alphabet, text, key):
        code = self.__polybius.encrypt(text, alphabet=alphabet)
        even = ""
        odd = ""
        rem = len(code) % (key << 1)
        for i in range(0, len(code)-rem, key << 1):
            ikey = i+key
            even += code[i:ikey]
            odd += code[ikey:ikey+key]

        even += code[-rem:-(rem >> 1)]
        odd += code[-(rem >> 1):]

        code = ""
        for i in range(len(even)):
            code += even[i] + odd[i]
        return self.__polybius.decrypt(code, alphabet=alphabet)

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
        key = int(key)
        if not key > 0:
            key = len(text)
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
        key = int(key)
        if not key > 0:
            key = len(text)
        return self.__dec(alphabet, text, key)
