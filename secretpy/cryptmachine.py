#!/usr/bin/python

class CryptMachine:
	def __init__(self, cipher, key=None, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		self.alphabet = alphabet
		self.key = key or ""
		self.cipher = cipher

	def setKey(self, key):
		self.key = key

	def setAlphabet(self, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		self.alphabet = alphabet
	
	def setCipher(self, cipher):
		self.cipher = cipher
		
	def encrypt(self, text):
		res = self.cipher.encrypt(text, self.key, self.alphabet)
		return res
		
	def decrypt(self, text):
		res = self.cipher.decrypt(text, self.key, self.alphabet)
		return res
