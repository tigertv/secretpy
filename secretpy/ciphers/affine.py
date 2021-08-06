#!/usr/bin/python
from secretpy import alphabets as al


class Affine:
    """
    The Affine Cipher
    """

    def encrypt(self, text, key, alphabet=al.ENGLISH):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key constisting of two parts: a and b. GCD(a, length of alphabet) = 1
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: tuple of 2 integers
        :type alphabet: string
        :return: text
        :rtype: string
        """
        a = key[0]
        b = key[1]
        subst = {c: alphabet[(i * a + b) % len(alphabet)][0] for i, letters in enumerate(alphabet) for c in letters}
        res = []
        try:
            for t in text:
                res.append(subst[t])
        except KeyError:
            wrchar = t.encode('utf-8')
            raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
        return "".join(res)

    def decrypt(self, text, key, alphabet=al.ENGLISH):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key constisting of two parts: a and b. GCD(a, length of alphabet) = 1
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: tuple of 2 integers
        :type alphabet: string
        :return: text
        :rtype: string
        """
        a = self.__inverse(key[0], len(alphabet))
        b = - key[1] * a
        inverse_key = (a, b)
        return self.encrypt(text, inverse_key, alphabet)

    def __inverse(self, a, m):
        if (m == 1 or a == 0):
            return 0
        a %= m

        mm = m
        y = 0
        x = 1
        # Extended Euclid Algorithm
        while a > 1:
            q, temp = divmod(a, mm)
            a, mm = mm, temp
            y, x = x - q * y, y
        if (x < 0):
            x += m
        return x
