#!/usr/bin/python
# -*- encoding: utf-8 -*-

class AbstractMachineDecorator:
	def __init__(self, machine):
		self.machine = machine 

	def setKey(self, key):
		self.machine.setKey(key)

	def setAlphabet(self, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		self.machine.setAlphabet(alphabet)
	
	def setCipher(self, cipher):
		self.machine.setCipher(cipher)
		
	def encrypt(self, text):
		pass
		
	def decrypt(self, text):
		pass
