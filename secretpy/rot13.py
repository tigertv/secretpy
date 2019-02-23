#!/usr/bin/python

from .caesar import Caesar

class Rot13:
	__caesar = Caesar()
	__alphabet = u"abcdefghijklmnopqrstuvwxyz"

	def __encDec(self, alphabet, text, isEncrypt):
		key = len(alphabet) >> 1
		ret = ""
		if isEncrypt == 1:
			ret = self.__caesar.encrypt(text, key, alphabet)
		else:
			ret = self.__caesar.decrypt(text, key, alphabet)
		return ret

	def encrypt(self, text, key=None, alphabet=None):
		alphabet = alphabet or self.__alphabet
		return self.__encDec(alphabet, text, 1)

	def decrypt(self, text, key=None, alphabet=None):
		alphabet = alphabet or self.__alphabet
		return self.__encDec(alphabet, text, -1)


