#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator


class SaveCase(AbstractMachineDecorator):

    def encrypt(self, text):
        return self.__encDec(text, lambda text: self._machine.encrypt(text))

    def decrypt(self, text):
        return self.__encDec(text, lambda text: self._machine.decrypt(text))

    def __encDec(self, text, func):
        uppercases = []
        for i, char in enumerate(text):
            if char == char.upper():
                uppercases.append(i)
        text = text.lower()
        res = func(text)
        for i in uppercases:
            res = res[:i] + res[i].upper() + res[i+1:]
        return res
