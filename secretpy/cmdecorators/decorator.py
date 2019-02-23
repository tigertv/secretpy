#!/usr/bin/python
# -*- encoding: utf-8 -*-

from ..abstractmachine import AbstractCryptMachine

class AbstractMachineDecorator(AbstractCryptMachine):
	def __init__(self, machine):
		self._machine = machine 

	def setKey(self, key):
		self._machine.setKey(key)

	def setAlphabet(self, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		self._machine.setAlphabet(alphabet)
	
	def setCipher(self, cipher):
		self._machine.setCipher(cipher)
		
	def encrypt(self, text):
		pass
		
	def decrypt(self, text):
		pass
