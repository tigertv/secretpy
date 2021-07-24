#!/usr/bin/python
from secretpy import alphabets as al


class Atbash:
    """
    The Atbash Cipher
    """

    def __crypt(self, alphabet, text):
        subst = {c: alphabet[len(alphabet) - i - 1][0] for i, letters in enumerate(alphabet) for c in letters}
        res = []
        try:
            for t in text:
                res.append(subst[t])
        except ValueError:
            wrchar = t.encode('utf-8')
            raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
        return "".join(res)

    def encrypt(self, text, key=None, alphabet=al.ENGLISH):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: is not used
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string or tuple of strings
        :return: text
        :rtype: string
        """
        return self.__crypt(alphabet, text)

    def decrypt(self, text, key=None, alphabet=al.ENGLISH):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: is not used
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string or tuple of strings
        :return: text
        :rtype: string
        """
        return self.__crypt(alphabet, text)
