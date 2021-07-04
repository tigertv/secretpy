#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator


class SaveCase(AbstractMachineDecorator):

    def encrypt(self, text):
        return self.__crypt(text, self._machine.encrypt)

    def decrypt(self, text):
        return self.__crypt(text, self._machine.decrypt)

    def __crypt(self, text, func):
        uppercases = [i for i, char in enumerate(text) if char == char.upper()]
        text = text.lower()

        res = func(text)
        res = list(res)

        for i in uppercases:
            res[i] = res[i].upper()
        return u"".join(res)
