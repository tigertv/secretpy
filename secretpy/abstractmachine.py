#!/usr/bin/python

class AbstractCryptMachine:
	def setKey(self, key):
		pass

	def setAlphabet(self, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		pass
	
	def setCipher(self, cipher):
		pass
		
	def encrypt(self, text):
		pass
		
	def decrypt(self, text):
		pass
