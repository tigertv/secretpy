#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator


class Block(AbstractMachineDecorator):

    def __init__(self, machine, length=5, sep=" "):
        self.length = length
        self.sep = sep
        super(Block, self).__init__(machine)

    def encrypt(self, text):
        txt = self._machine.encrypt(text.lower())
        return self.sep.join(txt[i:i + self.length] for i in range(0, len(txt), self.length))

    def decrypt(self, text):
        # remove separator
        step = self.length + len(self.sep)
        txt = "".join(text[i:i + self.length] for i in range(0, len(text), step))
        return self._machine.decrypt(txt.lower())
