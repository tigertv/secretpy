#!/usr/bin/python
# -*- encoding: utf-8 -*-
from collections import OrderedDict


class Keyword:
    """
    The Keyword Cipher
    """

    def __crypt(self, alphabet, key, text, is_encrypt):
        # remove repeats of letters in the key
        newkey = "".join(OrderedDict.fromkeys(key))
        # create the substitution string
        longkey = "".join(OrderedDict.fromkeys(newkey+"".join(alphabet)))
        # do encryption
        res = []
        for i, t in enumerate(text):
            try:
                if is_encrypt == 1:
                    index = alphabet.index(t)
                    enc = longkey[index]
                else:
                    index = longkey.index(t)
                    enc = alphabet[index]
            except ValueError:
                wrchar = t.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            res.append(enc)
        return "".join(res)

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
        return self.__crypt(alphabet, key, text, 1)

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
        return self.__crypt(alphabet, key, text, -1)
