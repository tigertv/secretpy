#!/usr/bin/python


class Atbash:
    """
    The Atbash Cipher
    """

    def __encDec(self, alphabet, text):
        ans = ""
        for char in text:
            alphIndex = len(alphabet) - (alphabet.index(char)) - 1
            enc = alphabet[alphIndex]
            ans += enc
        return ans

    def encrypt(self, text, key=None, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
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
        return self.__encDec(alphabet, text)

    def decrypt(self, text, key=None, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return self.__encDec(alphabet, text)
