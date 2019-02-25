#!/usr/bin/python

from .rot13 import Rot13

class Rot47:
	__rot13= Rot13()

	def __init__(self):
		self.__alphabet = "".join([chr(asc) for asc in range(33, 33 + 47*2 )])

	def __encDec(self, text):
		return self.__rot13.encrypt(text, alphabet=self.__alphabet)

	def encrypt(self, text, key=None, alphabet=None):
		return self.__encDec(text)

	def decrypt(self, text, key=None, alphabet=None):
		return self.__encDec(text)


