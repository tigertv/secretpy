#!/usr/bin/python
# -*- encoding: utf-8 -*-

class AbstractMachineDecorator:
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
