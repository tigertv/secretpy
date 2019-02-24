#!/usr/bin/python

from .caesar import Caesar

class Rot13:
	__caesar = Caesar()
	__alphabet = u"abcdefghijklmnopqrstuvwxyz"

	def __encDec(self, alphabet, text):
		alphabet = alphabet or self.__alphabet
		key = (int)(len(alphabet) / 2) 
		if len(alphabet) % 2 == 1:
			key += 1
			alphabet += alphabet[key-1]
		ret = self.__caesar.encrypt(text, key, alphabet)
		return ret

	def encrypt(self, text, key=None, alphabet=None):
		return self.__encDec(alphabet, text)

	def decrypt(self, text, key=None, alphabet=None):
		return self.__encDec(alphabet, text)


