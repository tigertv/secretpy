#!/usr/bin/python
# -*- encoding: utf-8 -*-
from collections import OrderedDict
from secretpy import alphabets as al


class Keyword:
    """
    The Keyword Cipher
    """

    def __crypt(self, alphabet, key, text, is_encrypt):
        indexes = {c: i for i, letters in enumerate(alphabet) for c in letters}
        # remove duplicates
        keyi = OrderedDict.fromkeys(indexes[char] for char in key)
        new_key = [alphabet[i] for i in keyi]
        for i, a in enumerate(alphabet):
            if i not in keyi:
                new_key.append(a[0])

        if is_encrypt:
            subst = {c: new_key[i] for c, i in indexes.items()}
        else:
            subst = {c: alphabet[i][0] for i, letters in enumerate(new_key) for c in letters}
        # do encryption
        res = []
        for t in text:
            try:
                res.append(subst[t])
            except KeyError:
                wrchar = t.encode('utf-8')
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
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return self.__crypt(alphabet, key, text, True)

    def decrypt(self, text, key, alphabet=al.ENGLISH):
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
        return self.__crypt(alphabet, key, text, False)
