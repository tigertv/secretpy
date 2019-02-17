#!/usr/bin/python
# -*- encoding: utf-8 -*-

from .decorator import AbstractMachineDecorator

class UpperCase(AbstractMachineDecorator):

	def encrypt(self, text):
		text = text.lower()
		res = self.machine.encrypt(text)
		return res.upper()

	def decrypt(self, text):
		text = text.lower()
		res = self.machine.decrypt(text)
		return res.upper()
