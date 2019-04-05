#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator


class UpperCase(AbstractMachineDecorator):

    def encrypt(self, text):
        text = text.lower()
        res = self._machine.encrypt(text)
        return res.upper()

    def decrypt(self, text):
        text = text.lower()
        res = self._machine.decrypt(text)
        return res.upper()
