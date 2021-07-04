#!/usr/bin/python
# -*- encoding: utf-8 -*-

import secretpy.alphabets as al
from itertools import chain, cycle


class CaesarProgressive:
    """
    The Caesar Progressive Cipher
    """

    def __crypt(self, alphabet, key, text, is_encrypt):
        # key should be between 0 and len(alphabet)
        key %= len(alphabet)
        # prepare alphabet for substitution
        subst = {c: i for i, letters in enumerate(alphabet) for c in letters}
        res = []
        ch = chain(range(key, len(alphabet)), range(key))
        for k, t in zip(cycle(ch), text):
            try:
                i = (subst[t] + is_encrypt * k) % len(alphabet)
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
        return self.__crypt(alphabet, key, text, 1)

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
        return self.__crypt(alphabet, key, text, -1)
