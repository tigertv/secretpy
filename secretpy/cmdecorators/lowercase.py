#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator


class LowerCase(AbstractMachineDecorator):

    def encrypt(self, text):
        return self._machine.encrypt(text.lower())

    def decrypt(self, text):
        return self._machine.decrypt(text.lower())
