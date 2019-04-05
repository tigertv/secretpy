#!/usr/bin/python

from .abstractmachine import AbstractCryptMachine


class CompositeMachine(AbstractCryptMachine):
    __machines = []

    def __init__(self, *machines):
        for machine in machines:
            self.__machines.append(machine)

    def __encDec(self, text, func):
        ret = text
        for machine in self.__machines:
            ret = func(machine, ret)
        return ret

    def encrypt(self, text):
        return self.__encDec(text, lambda machine, text: machine.encrypt(text))

    def decrypt(self, text):
        return self.__encDec(text, lambda machine, text: machine.decrypt(text))

    def add_machines(self, *machines):
        for machine in machines:
            self.__machines.append(machine)
