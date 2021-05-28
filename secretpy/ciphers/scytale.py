#!/usr/bin/python
# -*- encoding: utf-8 -*-

import secretpy.alphabets as al


class Scytale:
    """
    The Scytale Cipher
    """
    __alphabet = al.ENGLISH

    def __enc(self, text, key, alphabet):
        block_list = []
        ans = ""
        rows = 0

        # Round up number of "rows"
        # "ceil(len(text) / key" not possible due to compatibility to python 2
        if (len(text) % key) != 0:
            rows = int((len(text) / key) + 1)
        else:
            rows = int(len(text) / key)

        # split text into blocks (row by row)
        for i in range(0, rows):
            if ((i * key) + key) <= len(text):
                block_list.append(text[(i * key):((i * key) + key)])
            else:
                block_list.append(text[(i * key):len(text)])

        # read characters from blocks
        for char in range(0, key):
            for block in range(0, rows):
                try:
                    ans = ans + block_list[block][char]
                except:
                    break
        return ans

    def __dec(self, text, key, alphabet):
        block_list = []
        ans = ""
        rows = 0
        additional_chars = len(text) % key
        block_start = 0
        block_end = 0

        # Round up number of "rows" and "block_end"
        # "ceil(len(text) / key" not possible due to compatibility to python 2
        if (len(text) % key) != 0:
            rows = int((len(text) / key) + 1)
            block_end = int((len(text) / key) + 1)
        else:
            rows = int(len(text) / key)
            block_end = int(len(text) / key)

        # split text into blocks (column by column)
        for i in range(0, key):
            # If scytale is fully occupied
            if (rows * key) == len(text):
                block_list.append(text[block_start:block_end])
                block_start = block_start + rows
                block_end = block_end + rows
            # If scytale is NOT fully occupied (last row has empty places)
            elif additional_chars > 1:
                block_list.append(text[block_start:block_end])
                additional_chars = additional_chars - 1
                block_start = block_start + rows
                block_end = block_end + rows
            elif additional_chars == 1:
                block_list.append(text[block_start:block_end])
                additional_chars = additional_chars - 1
                block_start = block_start + rows
                block_end = block_end + (rows - 1)
            elif additional_chars == 0:
                block_list.append(text[block_start:block_end])
                block_start = block_start + (rows - 1)
                block_end = block_end + (rows - 1)

        # read characters from blocks
        for char in range(0, rows):
            for block in range(0, key):
                try:
                    ans = ans + block_list[block][char]
                except:
                    break
        return ans

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
