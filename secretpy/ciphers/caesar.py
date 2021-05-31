#!/usr/bin/python
# -*- encoding: utf-8 -*-

import secretpy.alphabets as al


class Caesar:
    """
    The Caesar Cipher
    """
    __alphabet = al.ENGLISH

    def __crypt(self, alphabet, key, text):
        alph = alphabet or self.__alphabet
        res = []
        for c in text:
            try:
                index = alph.index(c)
            except ValueError:
                wrchar = c.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            index = (index + key) % len(alph)
            res.append(alph[index])
        return "".join(res)

    def encrypt(self, text, key, alphabet=None):
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
        return self.__crypt(alphabet, key, text)

    def decrypt(self, text, key, alphabet=None):
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
        return self.__crypt(alphabet, -key, text)
