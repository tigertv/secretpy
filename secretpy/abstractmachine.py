#!/usr/bin/python


class AbstractCryptMachine(object):
    def set_key(self, key):
        pass

    def set_alphabet(self, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
        pass

    def get_alphabet(self):
        pass

    def set_cipher(self, cipher):
        pass

    def encrypt(self, text):
        pass

    def decrypt(self, text):
        pass
