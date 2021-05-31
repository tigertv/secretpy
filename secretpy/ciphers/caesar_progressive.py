#!/usr/bin/python
# -*- encoding: utf-8 -*-

import secretpy.alphabets as al


class CaesarProgressive:
    """
    The Caesar Progressive Cipher
    """

    def __crypt(self, alphabet, key, text, isEncrypt):
        alph = alphabet or al.ENGLISH
        res = []
        for i, char in enumerate(text):
            try:
                index = alph.index(char)
            except ValueError as e:
                wrchar = char.encode('utf-8')
                e.args = (
                    "Can't find char '" + wrchar + "' of text in alphabet!",)
                raise
            index = (index + isEncrypt * (key + i)) % len(alph)
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
        return self.__crypt(alphabet, key, text, 1)

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
        return self.__crypt(alphabet, key, text, -1)
