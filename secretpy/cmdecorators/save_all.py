#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator


class SaveAll(AbstractMachineDecorator):

    def encrypt(self, text):
        return self.__crypt(text, self._machine.encrypt)

    def decrypt(self, text):
        return self.__crypt(text, self._machine.decrypt)

    def __crypt(self, text, func):
        # make lower case and save indexes
        upcases = [i for i, char in enumerate(text) if char.isupper()]
        txt = list(text)
        for i in upcases:
            txt[i] = txt[i].lower()

        # remove non-alphabet characters and save indexes
        alphabet = self._machine.get_alphabet()
        coords = {c: i for i, letters in enumerate(alphabet) for c in letters}
        chars = [i for i, char in enumerate(txt) if char not in coords]
        for i in reversed(chars):
            del txt[i]

        # execute function
        res = func("".join(txt))
        res = list(res)

        # restore non-alphabet characters
        for i in chars:
            res.insert(i, text[i])

        # restore uppercase
        for i in upcases:
            res[i] = res[i].upper()

        return "".join(res)
