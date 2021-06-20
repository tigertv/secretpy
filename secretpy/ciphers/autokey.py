#!/usr/bin/python
# -*- encoding: utf-8 -*-


class Autokey:
    """
    The Autokey Cipher
    """

    def __crypt(self, alphabet, key, text, is_encrypt):
        res = []
        for i, t in enumerate(text):
            try:
                a_index = alphabet.index(t)
            except ValueError:
                wrchar = t.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            if i < len(key):
                k = key[i]
            else:
                if is_encrypt == 1:
                    k = text[i - len(key)]
                else:
                    k = res[i - len(key)]
            try:
                a_index += is_encrypt * alphabet.index(k)
            except ValueError:
                wrchar = k.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            a_index = a_index % len(alphabet)
            enc = alphabet[a_index]
            res.append(enc)
        return "".join(res)

    def encrypt(self, text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
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
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return self.__crypt(alphabet, key, text, -1)
