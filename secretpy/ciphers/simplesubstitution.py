#!/usr/bin/python
# -*- encoding: utf-8 -*-


class SimpleSubstitution:
    """
    The Simple Substitution Cipher
    """

    def __encDec(self, alphabet, key, text, isEncrypt):
        if len(alphabet) != len(key):
            return

        ans = ""
        for i in range(len(text)):
            m = text[i]
            k = ""
            if isEncrypt == 1:
                k = key[alphabet.index(m)]
            else:
                k = alphabet[key.index(m)]
            ans += k
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
