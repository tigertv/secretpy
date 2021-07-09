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
        full_rows, rmd = len(text) // key, len(text) % key
        rows = full_rows + (rmd > 0)
        index = rows * rmd
        res = [text[i:index:rows] for i in range(rows)]
        add_res = [res[i] + text[index+i::full_rows] for i in range(full_rows)]
        if rmd:
            add_res.append(res[-1])
        return "".join(add_res)
