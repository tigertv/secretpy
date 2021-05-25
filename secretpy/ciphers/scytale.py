#!/usr/bin/python
# -*- encoding: utf-8 -*-

import secretpy.alphabets as al
from math import ceil, floor


class Scytale:
    """
    The Scytale Cipher
    """

    __alphabet = al.ENGLISH

    def __enc(self, alphabet, key, text):
        alphabet = alphabet or self.__alphabet
        ans = ""

        for char in text:
            try:
                alphabet.index(char)
            except ValueError:
                raise Exception("Can't find char '" + char + "' of text in alphabet!")

        # Loop for every char inside a block
        for char_count in range(0, key):
            # Loop for every block defined by key
            for block_count in range(0, ceil(len(text) / key)):
                if (char_count + (block_count * key)) < len(text):
                    ans = ans + text[char_count + (block_count * key)]
                else:  # Break loop if last block is not full
                    break
        return ans

    def __dec(self, alphabet, key, text):
        alphabet = alphabet or self.__alphabet
        ans = ""

        for char in text:
            try:
                alphabet.index(char)
            except ValueError:
                raise Exception("Can't find char '" + char + "' of text in alphabet!")

        # Loop for every char inside a block
        for char_count in range(0, ceil(len(text) / key)):
            shift = 0  # Shift for blocks with different sizes
            # Loop for every block defined by key
            for block_count in range(0, key):
                # Check if current char index is outside text length
                if (char_count * key + shift) < len(text):
                    ans = ans + text[char_count + (block_count * (floor(len(text) / key))) + shift]
                    if shift < (len(text) % key):
                        shift = shift + 1
                else:  # Break loop if text length is reached
                    break
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
        :rtype string
        """
        return self.__enc(alphabet, key, text)

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
        :rtype string
        """

        return self.__dec(alphabet, key, text)