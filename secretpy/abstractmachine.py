#!/usr/bin/python


class AbstractCryptMachine:
    def set_key(self, key):
        pass

    def set_alphabet(self, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
        pass

    def set_cipher(self, cipher):
        pass

    def encrypt(self, text):
        pass

    def decrypt(self, text):
        pass
