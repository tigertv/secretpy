#!/usr/bin/python

class CryptMachine:
	def __init__(self, cipher, key=None, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		self.alphabet = alphabet
		self.key = key or ""
		self.cipher = cipher
		self.uppercase = False

	def setKey(self, key):
		self.key = key

	def setAlphabet(self, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		self.alphabet = alphabet
	
	def setCipher(self, cipher):
		self.cipher = cipher
		
	def encrypt(self, text):
		if self.uppercase:
			text = text.lower()
		res = self.cipher.encrypt(text, self.key, self.alphabet)
		if self.uppercase:
			res = res.upper()
		return res
		
	def decrypt(self, text):
		if self.uppercase:
			text = text.lower()
		res = self.cipher.decrypt(text, self.key, self.alphabet)
		if self.uppercase:
			res = res.upper()
		return res
	
	def setUpperCase(self):
		self.uppercase = True

	def resetUpperCase(self):
		self.uppercase = False

