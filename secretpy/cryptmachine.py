#!/usr/bin/python

from .abstractmachine import AbstractCryptMachine
from secretpy import alphabets as al


class CryptMachine(AbstractCryptMachine):
    def __init__(self, cipher, key="", alphabet=al.ENGLISH):
        self.__key = key
        self.set_cipher(cipher)
        self.set_alphabet(alphabet)

    def __define_mixedcase(self, alphabet):
        # check upper case letters
        has_upper = False
        has_lower = False

        for letters in alphabet:
            for c in letters:
                if c.isupper():
                    has_upper = True
                elif c.lower():
                    has_lower = True

        if has_upper and has_lower:
            self.__alphabet = alphabet
            self.mixedcase = True
        elif has_upper and not has_lower:
            self.__alphabet = alphabet.lower()
            self.mixedcase = False
        else:
            self.__alphabet = alphabet
            self.mixedcase = False

    def set_key(self, key):
        self.__key = key

    def set_alphabet(self, alphabet=al.ENGLISH):
        if hasattr(self.__cipher, 'get_fixed_alphabet'):
            return
        self.__define_mixedcase(alphabet)

    def get_alphabet(self):
        return self.__alphabet

    def set_cipher(self, cipher):
        self.__cipher = cipher
        if not hasattr(cipher, 'get_fixed_alphabet'):
            return
        alphabet = cipher.get_fixed_alphabet()
        self.__define_mixedcase(alphabet)

    # returns True if mixedcase in alphabet, False otherwise
    def has_mixedcase(self):
        return self.mixedcase

    def encrypt(self, text):
        alphabet = self.__alphabet
        return self.__crypt(text, self.__cipher.encrypt, alphabet)

    def get_crypt_alphabet(self):
        if hasattr(self.__cipher, 'get_crypt_alphabet'):
            alphabet = self.__cipher.get_crypt_alphabet()
        else:
            alphabet = self.__alphabet
        return alphabet

    def decrypt(self, text):
        alphabet = self.get_crypt_alphabet()
        return self.__crypt(text, self.__cipher.decrypt, alphabet)

    def __crypt(self, text, func, alphabet):
        # prepare alphabet
        alpha = {c: 1 for letters in alphabet for c in letters}
        if not self.mixedcase:
            txt = text.lower()
        else:
            txt = text
        # filter text by alphabet
        txt = "".join(filter(lambda c: c in alpha, txt))
        return func(txt, self.__key, self.__alphabet)
