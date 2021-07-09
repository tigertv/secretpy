#!/usr/bin/python
# -*- encoding: utf-8 -*-


class Zigzag:
    """
    The Zigzag Cipher (Rail-Fence)
    """

    def encrypt(self, text, key, alphabet=None):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: unused
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        if key <= 0:
            return
        key0 = key - 1
        step = key0 << 1

        # the first row
        crypted = [text[::step]]

        # next rows
        textlen = len(text)
        for row in range(1, key0):
            right = step - row
            for left in range(row, textlen, step):
                crypted.append(text[left])
                if right < textlen:
                    crypted.append(text[right])
                right += step
        # the last row
        crypted.append(text[key0::step])
        return "".join(crypted)

    def decrypt(self, text, key, alphabet=None):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: unused
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        step = (key - 1) << 1
        textlen = len(text)
        decrypted = [None] * textlen

        # first row
        i = 0
        for left in range(0, textlen, step):
            decrypted[left] = text[i]
            i += 1

        # next rows
        for row in range(1, key):
            for left in range(row, textlen, step):
                decrypted[left] = text[i]
                i += 1
                right = left + step - (row << 1)
                if right < textlen and right != left:
                    decrypted[right] = text[i]
                    i += 1

        return "".join(decrypted)
