#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator


class UpperCase(AbstractMachineDecorator):

    def encrypt(self, text):
        return self._machine.encrypt(text).upper()

    def decrypt(self, text):
        return self._machine.decrypt(text).upper()
