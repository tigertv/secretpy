#!/usr/bin/python
# -*- encoding: utf-8 -*-

from ..abstractmachine import AbstractCryptMachine
from secretpy import alphabets


class AbstractMachineDecorator(AbstractCryptMachine):
    def __init__(self, machine):
        self._machine = machine

    def set_key(self, key):
        self._machine.set_key(key)

    def set_alphabet(self, alphabet=alphabets.ENGLISH):
        self._machine.set_alphabet(alphabet)

    def get_alphabet(self):
        return self._machine.get_alphabet()

    def get_crypt_alphabet(self):
        return self._machine.get_crypt_alphabet()

    def set_cipher(self, cipher):
        self._machine.set_cipher(cipher)

    def has_mixedcase(self):
        return self._machine.has_mixedcase()

    def encrypt(self, text):
        pass

    def decrypt(self, text):
        pass
