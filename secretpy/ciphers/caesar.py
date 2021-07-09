#!/usr/bin/python
# -*- encoding: utf-8 -*-

import secretpy.alphabets as al
from itertools import chain


class Caesar:
    """
    The Caesar Cipher
    """

    def __crypt(self, key, text, alphabet):
        # key should be between 0 and len(alphabet)
        key %= len(alphabet)
        # prepare alphabet for substitution
        ch = chain(range(key, len(alphabet)), range(key))
        subst = {c: alphabet[i][0] for i, letters in zip(ch, alphabet) for c in letters}
        res = []
        for c in text:
            try:
                res.append(subst[c])
            except KeyError:
                wrchar = c.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
        return u"".join(res)

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
        return self.__crypt(key, text, alphabet)

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
        return self.__crypt(-key, text, alphabet)
