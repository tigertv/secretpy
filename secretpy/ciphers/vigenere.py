#!/usr/bin/python
# -*- encoding: utf-8 -*-


class Vigenere:
    """
    The Vigenere Cipher
    """

    def __crypt(self, alphabet, key, text, is_encrypt):
        res = []
        for i, char in enumerate(text):
            keychar = key[i % len(key)]
            try:
                a_index = alphabet.index(char)
            except ValueError:
                wrchar = char.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            try:
                a_index += is_encrypt * alphabet.index(keychar)
            except ValueError:
                wrchar = keychar.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            a_index %= len(alphabet)
            res.append(alphabet[a_index])
        return "".join(res)

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
        return self.__crypt(alphabet, key, text, 1)

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
        return self.__crypt(alphabet, key, text, -1)
