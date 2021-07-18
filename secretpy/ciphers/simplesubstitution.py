#!/usr/bin/python
# -*- encoding: utf-8 -*-
from secretpy import alphabets as al


class SimpleSubstitution:
    """
    The Simple Substitution Cipher
    """
    def __crypt(self, subst, text):
        res = []
        for c in text:
            try:
                res.append(subst[c])
            except KeyError:
                wrchar = c.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
        return "".join(res)

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
        if len(alphabet) != len(key):
            raise Exception("Lengths of alphabet and key should be the same")
        # prepare alphabet for substitution
        subst = {a: k[0] for k, letters in zip(key, alphabet) for a in letters}
        return self.__crypt(subst, text)

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
        if len(alphabet) != len(key):
            raise Exception("Lengths of alphabet and key should be the same")
        # prepare alphabet for substitution
        subst = {k[0]: a[0] for k, a in zip(key, alphabet)}
        return self.__crypt(subst, text)
