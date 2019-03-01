#!/usr/bin/python

from .abstractmachine import AbstractCryptMachine
from secretpy import alphabet


class CryptMachine(AbstractCryptMachine):
    def __init__(self, cipher, key=None, alphabet=alphabet.ENGLISH):
        self.__alphabet = alphabet
        self.__key = key or ""
        self.__cipher = cipher

    def set_key(self, key):
        self.__key = key

    def set_alphabet(self, alphabet=alphabet.ENGLISH):
        self.__alphabet = alphabet

    def set_cipher(self, cipher):
        self.__cipher = cipher

    def encrypt(self, text):
        return self.__cipher.encrypt(text, self.__key, self.__alphabet)

    def decrypt(self, text):
        return self.__cipher.decrypt(text, self.__key, self.__alphabet)
