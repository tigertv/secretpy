#!/usr/bin/python

from .rot13 import Rot13
import secretpy.alphabet as al

class Rot5:
	__rot13= Rot13()
	__alphabet = al.DECIMAL

	def __encDec(self, text):
		return self.__rot13.encrypt(text, alphabet=self.__alphabet)

	def encrypt(self, text, key=None, alphabet=None):
		return self.__encDec(text)

	def decrypt(self, text, key=None, alphabet=None):
		return self.__encDec(text)
