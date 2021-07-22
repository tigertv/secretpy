#!/usr/bin/python
# -*- encoding: utf-8 -*-
from itertools import repeat
from secretpy import alphabets as al


class MyszkowskiTransposition:
    """
    The Myszkowski Transposition Cipher
    """
    def __keycols(self, key, alphabet):
        indexes = {c: i for i, letters in enumerate(alphabet) for c in letters}
        chars = [indexes[char] for char in key]
        chars = sorted(enumerate(chars), key=lambda x: x[1])
        cols = [[chars[0][0]]]

        for i in range(1, len(key)):
            if chars[i - 1][1] == chars[i][1]:
                cols[-1].append(chars[i][0])
            else:
                cols.append([chars[i][0]])
        return cols

    def encrypt(self, text, key, alphabet=al.ENGLISH):
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
        res = []
        keyorder = self.__keycols(key, alphabet)
        for columns in keyorder:
            if len(columns) == 1:
                res.append(text[columns[0]::len(key)])
            else:
                # use zip_longest in python3
                iterators = [iter(text[i::len(key)]) for i in columns]
                it_count = len(iterators)
                while it_count:
                    for i, it in enumerate(iterators):
                        try:
                            res.append(next(it))
                        except StopIteration:
                            it_count -= 1
                            iterators[i] = repeat('')
        return u"".join(res)

    def decrypt(self, text, key, alphabet=al.ENGLISH):
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
        cols = self.__keycols(key, alphabet)

        lines, rmd = divmod(len(text), len(key))
        lines += rmd > 0

        columns = [[] for _ in range(len(key))]
        texti = iter(text)
        # fill columns
        for col in cols:
            ccol = col
            for _ in range(lines):
                for i, value in enumerate(ccol):
                    if value < len(text):
                        columns[col[i]].append(next(texti))
                ccol = [i + len(key) for i in ccol]

        # read result from columns
        res = []
        iterators = [iter(column) for column in columns]
        loop = True
        while loop:
            for it in iterators:
                try:
                    res.append(next(it))
                except StopIteration:
                    loop = False
                    break
        return u"".join(res)
