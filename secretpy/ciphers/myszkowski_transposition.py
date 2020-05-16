#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import alphabets


class MyszkowskiTransposition:
    """
    The Myszkowski Transposition Cipher
    """
    def __enc(self, alphabet, key, text):
        chars = [alphabets.get_index_in_alphabet(char, alphabet)
                 for char in key]
        keyorder1 = sorted(enumerate(chars), key=lambda x: x[1])
        prev_key_char = ""
        cols = []
        col0 = []

        for i in range(len(key)):
            key_char = keyorder1[i][1]
            if prev_key_char != key_char:
                if len(col0) > 0:
                    cols.append(col0)
                col0 = []
                prev_key_char = key_char
            col0.append(text[keyorder1[i][0]::len(key)])

        if len(col0) > 0:
            cols.append(col0)

        ret = u""
        for col in cols:
            if len(col) == 1:
                ret += col[0]
            else:
                i = 0
                for i in range(len(col[0])):
                    for col0 in col:
                        try:
                            ret += col0[i]
                        except IndexError:
                            pass
        return ret

    def __dec(self, alphabet, key, text):
        chars = [alphabets.get_index_in_alphabet(char, alphabet)
                 for char in key]
        keyorder1 = sorted(enumerate(chars), key=lambda x: x[1])

        next_arr = []
        temp = []
        it = iter(keyorder1)
        try:
            prev, current = None, next(it)
            while True:
                prev = current
                temp.append(prev[0])
                current = next(it)
                if (prev and prev[1] != current[1]):
                    next_arr.append(temp)
                    temp = []
        except StopIteration:
            pass

        if len(temp) > 0:
            next_arr.append(temp)

        rmd, quotient = len(text) % len(key), int(len(text) / len(key))
        ret_arr = [None] * len(key)
        i = 0
        for ar in next_arr:
            len_sum = 0
            for index in ar:
                index_len = quotient
                if index < rmd:
                    index_len += 1

                len_sum += index_len
            tmp = text[int(i):int(i+len_sum)]
            i += len_sum
            for j, index in enumerate(ar):
                ret_arr[index] = tmp[j::len(ar)]

        ret = ""
        for row in range(0, quotient):
            for item in ret_arr:
                ret += item[row]

        row = quotient
        for i in range(0, rmd):
            ret += ret_arr[i][row]
        return ret

    def encrypt(self, text, key, alphabet=None):
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
        alphabet = alphabet or alphabets.ENGLISH
        return self.__enc(alphabet, key, text)

    def decrypt(self, text, key, alphabet=None):
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
        alphabet = alphabet or alphabets.ENGLISH
        return self.__dec(alphabet, key, text)
