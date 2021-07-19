#!/usr/bin/python
# -*- encoding: utf-8 -*-
from itertools import cycle
from secretpy import alphabets as al


class Porta:
    """
    The Porta Cipher
    """

    def encrypt(self, text, key, alphabet=al.ENGLISH):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: string
        :type alphabet: string
        :return: text
        :rtype: string
        """
        # prepare alphabet for substitution
        indexes = {c: i for i, letters in enumerate(alphabet) for c in letters}
        # prepare key
        key_indexes = (indexes[c] >> 1 for c in key)
        half = len(alphabet) >> 1
        res = []
        for t, k in zip(text, cycle(key_indexes)):
            try:
                texti = indexes[t]
            except ValueError:
                wrchar = t.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            if texti < half:
                i = (texti + k) % half + half
            else:
                i = (texti - k) % half
            res.append(alphabet[i][0])
        return u"".join(res)

    def decrypt(self, text, key, alphabet=al.ENGLISH):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: string
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return self.encrypt(text, key, alphabet)
