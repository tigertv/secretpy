#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .polybius_square import PolybiusSquare
from secretpy import alphabets as al


class Bifid:
    """
    The Bifid Cipher
    """

    def encrypt(self, text, key=None, alphabet=al.ENGLISH_SQUARE_IJ):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string or tuple or list
        :return: text
        :rtype: string
        """
        key = int(key)
        if key <= 0:
            key = len(text)
        square = PolybiusSquare(alphabet)
        coords = tuple(map(square.get_coordinates, text))
        res = []
        for i in range(0, len(coords), key):
            block = coords[i:i + key]
            block = list(zip(*block))
            block = block[0] + block[1]
            for j in range(1, len(block), 2):
                res.append(square.get_char(block[j - 1], block[j]))
        return "".join(res)

    def decrypt(self, text, key=None, alphabet=al.ENGLISH_SQUARE_IJ):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string or tuple or list
        :return: text
        :rtype: string
        """
        key = int(key)
        if key <= 0:
            key = len(text)
        square = PolybiusSquare(alphabet)
        coords = tuple(map(square.get_coordinates, text))
        res = []
        for i in range(0, len(coords), key):
            block = []
            for coord in coords[i:i + key]:
                block.append(coord[0])
                block.append(coord[1])
            half = len(block) // 2
            for row, column in zip(block[:half], block[half:]):
                res.append(square.get_char(row, column))
        return "".join(res)
