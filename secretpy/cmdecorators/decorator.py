#!/usr/bin/python
# -*- encoding: utf-8 -*-

from ..abstractmachine import AbstractCryptMachine

class AbstractMachineDecorator(AbstractCryptMachine):
	def __init__(self, machine):
		self._machine = machine 

	def set_key(self, key):
		self._machine.set_key(key)

	def set_alphabet(self, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		self._machine.set_alphabet(alphabet)
	
	def set_cipher(self, cipher):
		self._machine.set_cipher(cipher)
		
	def encrypt(self, text):
		pass
		
	def decrypt(self, text):
		pass
