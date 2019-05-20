#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import alphabets


class Porta:
    """
    The Porta Cipher
    """
    def __encDec(self, alphabet, key, text):
        ans = ""
        for i, char in enumerate(text):
            keychari = alphabet.index(key[i % len(key)]) >> 1
            textindex = alphabet.index(char)
            half = len(alphabet) >> 1
            half_alphabet = None
            if textindex < half:
                half_alphabet = alphabet[half:]
                alphIndex = (textindex + keychari) % half
            else:
                half_alphabet = alphabet[0:half]
                alphIndex = (textindex - keychari) % half
            ans += half_alphabet[alphIndex]
        return ans

    def encrypt(self, text, key, alphabet=alphabets.ENGLISH):
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
        return self.__encDec(alphabet, key, text)

    def decrypt(self, text, key, alphabet=alphabets.ENGLISH):
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

        return self.__encDec(alphabet, key, text)
