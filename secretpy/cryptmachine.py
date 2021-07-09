#!/usr/bin/python

from .abstractmachine import AbstractCryptMachine
from secretpy import alphabets


class CryptMachine(AbstractCryptMachine):
    def __init__(self, cipher, key=None, alphabet=alphabets.ENGLISH):
        self.__alphabet = alphabet
        self.__key = key or ""
        self.__cipher = cipher

    def set_key(self, key):
        self.__key = key

    def set_alphabet(self, alphabet=alphabets.ENGLISH):
        self.__alphabet = alphabet

    def get_alphabet(self):
        return self.__alphabet

    def set_cipher(self, cipher):
        self.__cipher = cipher

    def encrypt(self, text):
        return self.__crypt(text, self.__cipher.encrypt)

    def decrypt(self, text):
        return self.__crypt(text, self.__cipher.decrypt)

    def __crypt(self, text, func):
        # prepare alphabet
        alpha = {c: 1 for letters in self.__alphabet for c in letters}
        # filter text by alphabet
        txt = "".join(filter(lambda c: c in alpha, text.lower()))
        return func(txt, self.__key, self.__alphabet)
