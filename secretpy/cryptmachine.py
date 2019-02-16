#!/usr/bin/python

class CryptMachine:
	def __init__(self, key=None, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		self.alphabet = alphabet
		self.key = key or ""

	def setKey(self, key):
		self.key = key

	def setAlphabet(self, alphabet):
		self.alphabet = alphabet
	
	def setCipher(self, cipher):
		self.cipher = cipher
		
	def encrypt(self, text):
		return self.cipher.encrypt(text, self.key, self.alphabet)
		
	def decrypt(self, text):
		return self.cipher.decrypt(text, self.key, self.alphabet)
