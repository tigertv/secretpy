#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator


class RemoveNonAlphabet(AbstractMachineDecorator):

    def encrypt(self, text):
        return self.__crypt(text, self._machine.encrypt)

    def decrypt(self, text):
        return self.__crypt(text, self._machine.decrypt)

    def __crypt(self, text, func):
        alphabet = self._machine.get_alphabet()
        # prepare alphabet
        alpha = {c: 1 for letters in alphabet for c in letters}

        # filter text by alphabet
        res = filter(lambda char: char in alpha, text.lower())
        return func("".join(res))
