#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator


class NoSpaces(AbstractMachineDecorator):

    def encrypt(self, text):
        text = text.replace(" ", "")
        res = self._machine.encrypt(text)
        return res

    def decrypt(self, text):
        text = text.replace(" ", "")
        res = self._machine.decrypt(text)
        return res
