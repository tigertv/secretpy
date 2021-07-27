#!/usr/bin/python
# -*- encoding: utf-8 -*-


class Scytale:
    """
    The Scytale Cipher
    """

    def encrypt(self, text, key, alphabet=None):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key - Number of windings
        :param alphabet: Alphabet is not used
        :type text: string
        :type key: integer
        :return: encrypted text
        :rtype: string
        """
        # key is columns
        return "".join(text[i::key] for i in range(key))

    def decrypt(self, text, key, alphabet=None):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key - Number of windings
        :param alphabet: Alphabet is not used
        :type text: string
        :type key: integer
        :return: decrypted text
        :rtype: string
        """
        full_rows, rmd = divmod(len(text), key)
        rows = full_rows + (rmd > 0)
        middle = rows * rmd
        res = []
        for i in range(full_rows):
            res.append(text[i:middle:rows])
            res.append(text[middle + i::full_rows])
        res.append(text[full_rows:middle:rows])
        return "".join(res)
