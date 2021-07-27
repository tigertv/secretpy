#!/usr/bin/python
# -*- encoding: utf-8 -*-
from secretpy import alphabets as al


class ColumnarTransposition:
    """
    The Columnar Transposition Cipher
    """

    def __keyorder(self, alphabet, key):
        indexes = {c: i for i, letters in enumerate(alphabet) for c in letters}
        new_key = map(lambda x: indexes[x], key)
        return [i for i, _ in sorted(enumerate(new_key), key=lambda x: x[1])]

    def encrypt(self, text, key, alphabet=al.ENGLISH):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: string
        :type alphabet: string
        :return: text
        :rtype: string
        """
        keyorder = self.__keyorder(alphabet, key)
        return u"".join(text[i::len(key)] for i in keyorder)

    def decrypt(self, text, key, alphabet=al.ENGLISH):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: string
        :type alphabet: string
        :return: text
        :rtype: string
        """
        keyorder = self.__keyorder(alphabet, key)
        rows, rmd = divmod(len(text), len(key))

        p = []
        acc = 0
        for i in keyorder:
            p.append(acc)
            acc += rows
            if i < rmd:
                acc += 1

        roworder = [0] * len(key)
        for i, j in enumerate(keyorder):
            roworder[j] = p[i]

        res = [text[i + row] for row in range(rows) for i in roworder]
        # add tail(remainder) to the end of result
        for i in roworder[:rmd]:
            res.append(text[i + rows])
        return u"".join(res)
