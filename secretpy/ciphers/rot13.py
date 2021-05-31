#!/usr/bin/python

from .caesar import Caesar
import secretpy.alphabets as al


class Rot13:
    """
    The Rot13 Cipher (Half)
    """
    __caesar = Caesar()

    def __crypt(self, alphabet, text):
        alph = alphabet or al.ENGLISH
        key = len(alph) >> 1
        # if number of letters in the alphabet is odd
        if len(alph) & 1:
            alph += alph[key]
            key += 1
        return self.__caesar.encrypt(text, key, alph)

    def encrypt(self, text, key=None, alphabet=None):
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
        return self.__crypt(alphabet, text)

    def decrypt(self, text, key=None, alphabet=None):
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
        return self.__crypt(alphabet, text)
