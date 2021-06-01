#!/usr/bin/python
# -*- encoding: utf-8 -*-


class SimpleSubstitution:
    """
    The Simple Substitution Cipher
    """

    def encrypt(self, text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
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
        if len(alphabet) != len(key):
            return
        res = []
        for c in text:
            try:
                k = key[alphabet.index(c)]
            except ValueError:
                wrchar = c.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            res.append(k)
        return "".join(res)

    def decrypt(self, text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
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
        if len(alphabet) != len(key):
            return
        res = []
        for c in text:
            try:
                k = alphabet[key.index(c)]
            except ValueError:
                wrchar = c.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            res.append(k)
        return "".join(res)
