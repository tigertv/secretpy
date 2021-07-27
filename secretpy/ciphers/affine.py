#!/usr/bin/python
from secretpy import alphabets as al


class Affine:
    """
    The Affine Cipher
    """

    def __crypt(self, subst, text):
        res = []
        try:
            for t in text:
                res.append(subst[t])
        except KeyError:
            wrchar = t.encode('utf-8')
            raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
        return "".join(res)

    def __get_inverse(self, a, alphabet):
        for i in range(1, len(alphabet)):
            if (a * i) % len(alphabet) == 1:
                return i
        return 1

    def encrypt(self, text, key, alphabet=al.ENGLISH):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: tuple of 2 integers
        :type alphabet: string
        :return: text
        :rtype: string
        """
        a = int(key[0])
        b = int(key[1])
        subst = {c: alphabet[(i * a + b) % len(alphabet)][0] for i, letters in enumerate(alphabet) for c in letters}
        return self.__crypt(subst, text)

    def decrypt(self, text, key, alphabet=al.ENGLISH):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: tuple of 2 integers
        :type alphabet: string
        :return: text
        :rtype: string
        """
        a = int(key[0])
        b = int(key[1])
        a = self.__get_inverse(a, alphabet)
        subst = {c: alphabet[(a * (i - b)) % len(alphabet)][0] for i, letters in enumerate(alphabet) for c in letters}
        return self.__crypt(subst, text)
