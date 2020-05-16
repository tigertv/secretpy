#!/usr/bin/python
# -*- encoding: utf-8 -*-


class Autokey:
    """
    The Autokey Cipher
    """

    def __encDec(self, alphabet, key, text, isEncrypt):
        ans = ""
        for i in range(len(text)):
            m = text[i]
            if i < len(key):
                k = key[i]
            else:
                if isEncrypt == 1:
                    k = text[i - len(key)]
                else:
                    k = ans[i - len(key)]
            try:
                alphI = alphabet.index(m)
            except ValueError as e:
                wrchar = m.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            try:
                alphI += isEncrypt * alphabet.index(k)
            except ValueError as e:
                wrchar = k.encode('utf-8')
                raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
            alphI = alphI % len(alphabet)
            enc = alphabet[alphI]
            ans += enc
        return ans

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
        return self.__encDec(alphabet, key, text, 1)

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
        return self.__encDec(alphabet, key, text, -1)
