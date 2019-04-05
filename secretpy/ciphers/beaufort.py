#!/usr/bin/python
# -*- encoding: utf-8 -*-


class Beaufort:
    """
    The Beaufort Cipher
    """

    def __encDec(self, alphabet, key, text):
        ans = ""
        for i in range(len(text)):
            char = text[i]
            keychar = key[i % len(key)]
            alphIndex = (
                alphabet.index(keychar) - alphabet.index(char)
            ) % len(alphabet)
            ans += alphabet[alphIndex]
        return ans

    def encrypt(self, text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return self.__encDec(alphabet, key, text)

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
        return self.__encDec(alphabet, key, text)
