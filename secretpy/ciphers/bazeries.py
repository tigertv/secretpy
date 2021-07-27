#!/usr/bin/python
# -*- encoding: utf-8 -*-
from secretpy import alphabets as al
from .polybius_square import PolybiusSquare
from itertools import cycle


class Bazeries:
    """
    The Bazeries Cipher
    """

    def __crypt(self, alphabet, text, key, is_encrypt=True):
        # prepare digit key
        temp = key[0]
        digitkey = []
        while temp:
            temp, rmd = divmod(temp, 10)
            digitkey.append(rmd)
        digitkey = digitkey[::-1]

        # prepare text: reversion
        i = 0
        revtext = []
        digitkey = cycle(digitkey)
        while i < len(text):
            num = next(digitkey)
            s = text[i:i + num]
            revtext.append(s[::-1])
            i += num
        revtext = u"".join(revtext)

        sq1 = PolybiusSquare(alphabet)
        # key is a number, make it a string
        sq2 = PolybiusSquare(alphabet, key[1])
        if is_encrypt:
            sq1, sq2 = sq2, sq1

        # prepare substitution from alphabet
        subst = {c: sq1.get_char(*reversed(sq2.get_coordinates(c))) for letters in alphabet for c in letters}
        # cryption
        return u"".join(subst[t] for t in revtext)

    def encrypt(self, text, key, alphabet=al.ENGLISH_SQUARE_IJ):
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
        return self.__crypt(alphabet, text, key, True)

    def decrypt(self, text, key, alphabet=al.ENGLISH_SQUARE_IJ):
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
        return self.__crypt(alphabet, text, key, False)
