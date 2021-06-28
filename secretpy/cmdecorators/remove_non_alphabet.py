#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator


class RemoveNonAlphabet(AbstractMachineDecorator):

    def encrypt(self, text):
        return self.__crypt(text, lambda text: self._machine.encrypt(text))

    def decrypt(self, text):
        return self.__crypt(text, lambda text: self._machine.decrypt(text))

    def __crypt(self, text, func):
        alphabet = self._machine.get_alphabet()

        # filter text by alphabet
        if isinstance(alphabet, str):
            text2 = filter(lambda char: char in alphabet, text.lower())
        else:
            # for tuples or lists
            txt = []
            for c in text.lower():
                for a in alphabet:
                    if c in a:
                        txt.append(c)
            text2 = "".join(txt)

        return func(text2)
