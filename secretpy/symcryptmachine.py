#!/usr/bin/python

class SymCryptMachine:
	def __init__(self, alphabet, key):
		self.alphabet = alphabet
		self.key = key

	def setKey(self, key):
		self.key = key

	def setAlphabet(self, alphabet):
		self.alphabet = alphabet
	
	def setAlgorithm(self, algorithm):
		self.algorithm = algorithm
		
	def encrypt(self, plaintext):
		return self.algorithm.encrypt(self.alphabet, self.key, plaintext)
		
	def decrypt(self, ciphertext):
		return self.algorithm.decrypt(self.alphabet, self.key, ciphertext)
