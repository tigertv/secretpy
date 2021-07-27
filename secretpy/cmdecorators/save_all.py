#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator


class SaveAll(AbstractMachineDecorator):

    def encrypt(self, text):
        alphabet = self._machine.get_alphabet()
        return self.__crypt(text, self._machine.encrypt, alphabet)

    def decrypt(self, text):
        alphabet = self._machine.get_crypt_alphabet()
        return self.__crypt(text, self._machine.decrypt, alphabet)

    def __crypt(self, text, func, alphabet):
        # make lower case and save indexes
        txt = text
        if not self._machine.has_mixedcase():
            upcases = [i for i, c in enumerate(text) if c.isupper()]
            txt = txt.lower()

        # prepare alphabet
        alpha = {c: 1 for letters in alphabet for c in letters}

        # save indexes of non-alphabet characters
        chars = [i for i, c in enumerate(txt) if c not in alpha]

        # execute function
        res = list(func(txt))

        # restore non-alphabet characters
        for i in chars:
            res.insert(i, text[i])

        # restore uppercase
        if not self._machine.has_mixedcase():
            for i in filter(lambda x: x < len(res), upcases):
                res[i] = res[i].upper()

        return "".join(res)
