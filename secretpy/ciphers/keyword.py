#!/usr/bin/python
# -*- encoding: utf-8 -*-
from collections import OrderedDict


class Keyword:
    """
    The Keyword Cipher
    """

    def __removeDup(self, input_str):
        newstring = input_str[0]
        for i in range(len(input_str)):
            if newstring[(len(newstring) - 1)] != input_str[i]:
                newstring += input_str[i]
            else:
                pass
        return newstring

    def __encDec(self, alphabet, key, text, isEncrypt):
        # remove repeats of letters in the key
        newkey = "".join(OrderedDict.fromkeys(key))
        # create the substitution string
        longkey = "".join(OrderedDict.fromkeys(newkey+"".join(alphabet)))
        # do encryption
        ans = ""
        for i in range(len(text)):
            m = text[i]
            if isEncrypt == 1:
                index = alphabet.index(m)
                enc = longkey[index]
            else:
                index = longkey.index(m)
                enc = alphabet[index]
            ans += enc
        return ans

    def encrypt(self, text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
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
        return self.__encDec(alphabet, key, text, 1)

    def decrypt(self, text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
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
        return self.__encDec(alphabet, key, text, -1)
