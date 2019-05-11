#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .polybius_square import PolybiusSquare


class Bazeries:
    """
    The Bazeries Cipher
    """

    def __encDec(self, alphabet, text, key, isEncrypt=True):
        square1 = PolybiusSquare(alphabet)

        # key is a number, make it a string
        square2 = PolybiusSquare(alphabet, key[1])

        # prepare text: group and reverse
        temp = key[0]
        groups = []
        while temp > 0:
            rmd = temp % 10
            temp = int(temp / 10)
            groups.append(rmd)
        groups = groups[::-1]

        i = 0
        j = 0
        revtext = ""
        while i < len(text):
            num = groups[j]
            str1 = text[int(i):int(i+num)]
            revtext += str1[::-1]
            i += num
            j += 1
            if j == len(groups):
                j = 0

        # now we have reversed text and we encrypt
        ret = ""
        if isEncrypt:
            for char in revtext:
                coords = square1.get_coordinates(char)
                ret += square2.get_char(coords[1], coords[0])
        else:
            for char in revtext:
                coords = square2.get_coordinates(char)
                ret += square1.get_char(coords[1], coords[0])
        return ret

    def encrypt(self, text, key=None, alphabet=None):
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
        alphabet = alphabet or [
            u"a", u"b", u"c", u"d", u"e",
            u"f", u"g", u"h", u"ij", u"k",
            u"l", u"m", u"n", u"o", u"p",
            u"q", u"r", u"s", u"t", u"u",
            u"v", u"w", u"x", u"y", u"z"
        ]
        return self.__encDec(alphabet, text, key, True)

    def decrypt(self, text, key=None, alphabet=None):
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
        alphabet = alphabet or [
            u"a", u"b", u"c", u"d", u"e",
            u"f", u"g", u"h", u"ij", u"k",
            u"l", u"m", u"n", u"o", u"p",
            u"q", u"r", u"s", u"t", u"u",
            u"v", u"w", u"x", u"y", u"z"
        ]
        return self.__encDec(alphabet, text, key, False)
