#!/usr/bin/python

from .caesar import Caesar
import secretpy.alphabet as al

class Rot13:
	__caesar = Caesar()
	__alphabet = al.ENGLISH

	def __encDec(self, alphabet, text):
		alphabet = alphabet or self.__alphabet
		key = len(alphabet) >> 1
		# if number letters in the alphabet is odd
		if len(alphabet) & 1:
			alphabet += alphabet[key]
			key += 1
		return self.__caesar.encrypt(text, key, alphabet)

	def encrypt(self, text, key=None, alphabet=None):
		return self.__encDec(alphabet, text)

	def decrypt(self, text, key=None, alphabet=None):
		return self.__encDec(alphabet, text)


