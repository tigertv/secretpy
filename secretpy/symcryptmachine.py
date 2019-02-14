#!/usr/bin/python

class SymCryptMachine:
	def __init__(self, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		self.alphabet = alphabet
		self.key = key

	def setKey(self, key):
		self.key = key

	def setAlphabet(self, alphabet):
		self.alphabet = alphabet
	
	def setAlgorithm(self, algorithm):
		self.algorithm = algorithm
		
	def encrypt(self, plaintext):
		return self.algorithm.encrypt(self.key, plaintext, self.alphabet)
		
	def decrypt(self, ciphertext):
		return self.algorithm.decrypt(self.key, ciphertext, self.alphabet)
