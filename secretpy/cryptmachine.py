#!/usr/bin/python

from .abstractmachine import AbstractCryptMachine

class CryptMachine(AbstractCryptMachine):
	def __init__(self, cipher, key=None, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		self.__alphabet = alphabet
		self.__key = key or ""
		self.__cipher = cipher

	def setKey(self, key):
		self.__key = key

	def setAlphabet(self, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		self.__alphabet = alphabet
	
	def setCipher(self, cipher):
		self.__cipher = cipher
		
	def encrypt(self, text):
		return self.__cipher.encrypt(text, self.__key, self.__alphabet)
		
	def decrypt(self, text):
		return self.__cipher.decrypt(text, self.__key, self.__alphabet)
