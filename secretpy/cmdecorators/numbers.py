#!/usr/bin/python
# -*- encoding: utf-8 -*-
from .decorator import AbstractMachineDecorator


class Numbers(AbstractMachineDecorator):

    def __init__(self, machine, sep=' '):
        self.__sep = sep
        super(Numbers, self).__init__(machine)

    def encrypt(self, text):
        res = self._machine.encrypt(text)
        alphabet = self._machine.get_crypt_alphabet()
        subst = {t: str(i) for i, letters in enumerate(alphabet) for t in letters}
        return self.__sep.join(subst[t] for t in res)

    def decrypt(self, text):
        alphabet = self._machine.get_alphabet()
        subst = {str(i): letters[0] for i, letters in enumerate(alphabet)}
        # convert numbers to the characters of the alphabet
        txt = "".join(subst[i] for i in text.split(self.__sep))
        return self._machine.decrypt(txt)
