#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator


class SaveAll(AbstractMachineDecorator):

    def encrypt(self, text):
        return self.__encDec(text, lambda text: self._machine.encrypt(text))

    def decrypt(self, text):
        return self.__encDec(text, lambda text: self._machine.decrypt(text))

    def __encDec(self, text, func):
        chars = []
        upcases = []
        alphabet = self._machine.get_alphabet()
        text2 = text
        for i, char in enumerate(text2):
            if char.isupper():
                upcases.append(i)
        text2 = text2.lower()
        for i, char in enumerate(text2):
            if char not in alphabet:
                chars.append(i)
        for i in reversed(chars):
            text2 = text2[:i] + text2[i+1:]
        res = func(text2)
        for i in chars:
            res = res[:i] + text[i] + res[i:]
        for i in upcases:
            res = res[:i] + res[i].upper() + res[i+1:]
        return res
