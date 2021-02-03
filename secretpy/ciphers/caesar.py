#!/usr/bin/python
# -*- encoding: utf-8 -*-

import secretpy.alphabets as al


class Caesar:
    """
    The Caesar Cipher
    """
    __alphabet = al.ENGLISH

    def __encDec(self, alphabet, key, text, isEncrypt):
        alphabet = alphabet or self.__alphabet
        ans = ""
        for char in text:
            try:
                alphIndex = alphabet.index(char)
            except ValueError:
                wrchar = char.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            alphIndex = (alphIndex + isEncrypt * key) % len(alphabet)
            ans += alphabet[alphIndex]
        return ans

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
        return self.__encDec(alphabet, key, text, 1)

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
        return self.__encDec(alphabet, key, text, -1)
