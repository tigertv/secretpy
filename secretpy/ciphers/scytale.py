#!/usr/bin/python
# -*- encoding: utf-8 -*-

import secretpy.alphabets as al


class Scytale:
    """
    The Scytale Cipher
    """
    __alphabet = al.ENGLISH

    def __enc(self, text, key, alphabet):
        # key is columns
        return "".join(text[i::key] for i in range(key))

    def __dec(self, text, key, alphabet):
        full_rows, rmd = len(text) // key, len(text) % key
        rows = full_rows + (rmd > 0)
        b_index = rows * rmd
        res = [text[i:b_index:rows] for i in range(rows)]
        add_res = [res[i] + text[b_index+i::full_rows] for i in range(full_rows)]
        if rmd:
            add_res.append(res[-1])
        return "".join(add_res)

    def encrypt(self, text, key, alphabet=None):
        """
        Encryption method
        :param text: Text to encrypt
        :param key: Encryption key - Number of windings
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :return: encrypted text
        :rtype: string
        """
        return self.__enc(text, key, alphabet)

    def decrypt(self, text, key, alphabet=None):
        """
        Decryption method
        :param text: Text to decrypt
        :param key: Decryption key - Number of windings
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :return: decrypted text
        :rtype: string
        """
        return self.__dec(text, key, alphabet)
