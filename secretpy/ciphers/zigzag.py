#!/usr/bin/python
# -*- encoding: utf-8 -*-


class Zigzag:
    """
    The Zigzag Cipher
    """

    def __enc(self, key, text):
        crypted = ""
        step = (key - 1) << 1
        textlen = len(text)

        # first row
        left = 0
        while (left < textlen):
            crypted += text[left]
            left += step

        # next rows
        for row in range(1, key):
            left = row
            while (left < textlen):
                crypted += text[left]
                right = left + step - (row << 1)
                if right < textlen and right != left:
                    crypted += text[right]
                left += step

        return crypted

    def __dec(self, key, text):
        step = (key - 1) << 1
        textlen = len(text)
        decrypted = ["."] * textlen

        # first row
        left = 0
        i = 0
        while (left < textlen):
            decrypted[left] = text[i]
            left += step
            i += 1

        # next rows
        for row in range(1, key):
            left = row
            while (left < textlen):
                decrypted[left] = text[i]
                i += 1
                right = left + step - (row << 1)
                if right < textlen and right != left:
                    decrypted[right] = text[i]
                    i += 1
                left += step

        return "".join(decrypted)

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
        return self.__enc(key, text)

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
        return self.__dec(key, text)
