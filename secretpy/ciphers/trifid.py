#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import alphabets as al
from itertools import product


class Trifid:
    """
    The Trifid Cipher
    """
    alphabet = al.ENGLISH + "."

    def __code(self, text, alphabet):
        # prepare coordinates for each character in the alphabet
        # coord : (square, row, column)
        coords = {c: coord for i, coord in enumerate(product(range(3), repeat=3)) for c in alphabet[i]}
        code = []
        for char in text:
            code.extend(coords[char])
        return code

    def __decode(self, code, alphabet):
        text = []
        size = 3
        for i in range(0, len(code), size):
            index = code[i]  # square
            index = index * size + code[i + 1]  # row
            index = index * size + code[i + 2]  # column
            text.append(alphabet[index][0])
        return "".join(text)

    def encrypt(self, text, key=None, alphabet=None):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English with '.' is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        alphabet = alphabet or self.alphabet
        assert len(alphabet) == 27, "Length of the alphabet should be 27"

        size = 3
        key = int(key)
        if key <= 0:
            key = len(text)
        code = self.__code(text, alphabet)

        code0 = []
        for j in range(0, len(text) * size, size * key):
            for i in range(size):
                for item in code[j + i:j + size * key:size]:
                    code0.append(item)

        return self.__decode(code0, alphabet)

    def decrypt(self, text, key=None, alphabet=None):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English with '.' is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        alphabet = alphabet or self.alphabet
        assert len(alphabet) == 27, "Length of the alphabet should be 27"

        key = int(key)
        if key <= 0:
            key = len(text)
        code = self.__code(text, alphabet)

        size = 3
        res = []
        period = size * key
        for i in range(0, len(code), period):
            block = code[i:i + period]
            third = len(block) // size
            # coord : (square, row, column)
            for coord in zip(block[:third], block[third:2 * third], block[2 * third:]):
                res.extend(coord)
        return self.__decode(res, alphabet)
