#!/usr/bin/python
# -*- encoding: utf-8 -*-

import secretpy.alphabets as al
from itertools import chain, cycle


class CaesarProgressive:
    """
    The Caesar Progressive Cipher
    """

    def __crypt(self, alphabet, key, text):
        # prepare alphabet for substitution
        subst = {c: i for i, letters in enumerate(alphabet) for c in letters}
        res = []
        for t, k in zip(text, cycle(key)):
            try:
                i = subst[t] - k
            except KeyError:
                wrchar = t.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            res.append(alphabet[i][0])
        return "".join(res)

    def encrypt(self, text, key=3, alphabet=al.ENGLISH):
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
        :rtype: string
        """
        new_key = -key % len(alphabet)
        new_key = chain(range(new_key, -1, -1), range(len(alphabet) - 1, new_key, -1))
        return self.__crypt(alphabet, new_key, text)

    def decrypt(self, text, key=3, alphabet=al.ENGLISH):
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
        :rtype: string
        """
        new_key = key % len(alphabet)
        new_key = chain(range(new_key, len(alphabet)), range(new_key))
        return self.__crypt(alphabet, new_key, text)
