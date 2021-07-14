#!/usr/bin/python

from .abstractmachine import AbstractCryptMachine
from secretpy import alphabets


class CryptMachine(AbstractCryptMachine):
    def __init__(self, cipher, key="", alphabet=alphabets.ENGLISH):
        self.__key = key
        self.set_cipher(cipher)
        self.set_alphabet(alphabet)

    def set_key(self, key):
        self.__key = key

    def set_alphabet(self, alphabet=alphabets.ENGLISH):
        if hasattr(self.__cipher, 'get_fixed_alphabet'):
            return
        self.__alphabet = alphabet
        self.mixedcase = False

    def get_alphabet(self):
        return self.__alphabet

    def set_cipher(self, cipher):
        self.__cipher = cipher
        if not hasattr(self.__cipher, 'get_fixed_alphabet'):
            return
        alphabet = cipher.get_fixed_alphabet()
        # check upper case letters
        has_upper = False
        has_lower = False

        if isinstance(alphabet, str):
            for c in alphabet:
                if c.isupper():
                    has_upper = True
                elif c.lower():
                    has_lower = True
        else:
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

    # returns True if mixedcase in alphabet, False otherwise
    def has_mixedcase(self):
        return self.mixedcase

    def encrypt(self, text):
        return self.__crypt(text, self.__cipher.encrypt)

    def decrypt(self, text):
        return self.__crypt(text, self.__cipher.decrypt)

    def __crypt(self, text, func):
        # prepare alphabet
        alpha = {c: 1 for letters in self.__alphabet for c in letters}
        if not self.mixedcase:
            txt = text.lower()
        else:
            txt = text
        # filter text by alphabet
        txt = "".join(filter(lambda c: c in alpha, txt))
        return func(txt, self.__key, self.__alphabet)
