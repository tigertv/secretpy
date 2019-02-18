#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator

class SaveSpaces(AbstractMachineDecorator):

	def encrypt(self, text):
		func = lambda text : self._machine.encrypt(text)
		return self.__encDec(text , func)

	def decrypt(self, text):
		func = lambda text : self._machine.decrypt(text)
		return self.__encDec(text , func)

	def __encDec(self, text, func):
		spaces = []
		for i,char in enumerate(text):
			if char == ' ':	spaces.append(i)
		text = text.replace(" ", "")
		res = func(text)
		for i in spaces:
			res = res[:i] + ' ' + res[i:]
		return res
