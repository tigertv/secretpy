#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator


class UpperCase(AbstractMachineDecorator):

    def encrypt(self, text):
        res = self._machine.encrypt(text.lower())
        return res.upper()

    def decrypt(self, text):
        res = self._machine.decrypt(text.lower())
        return res.upper()
