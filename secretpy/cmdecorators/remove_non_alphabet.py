#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator


class RemoveNonAlphabet(AbstractMachineDecorator):

    def encrypt(self, text):
        return self.__encDec(text, lambda text: self._machine.encrypt(text))

    def decrypt(self, text):
        return self.__encDec(text, lambda text: self._machine.decrypt(text))

    def __encDec(self, text, func):
        alphabet = self._machine.get_alphabet()
        text2 = filter(lambda char: char in alphabet, text.lower())
        res = func(text2)
        return res
