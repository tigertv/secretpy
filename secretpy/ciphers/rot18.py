#!/usr/bin/python

from .rot13 import Rot13
import secretpy.alphabet as al

class Rot18:
	__rot13= Rot13()

	def __createAlphabet(self, alphabet):
		ahalf = len(alphabet) >> 1
		dhalf = len(al.DECIMAL) >> 1
		return alphabet[:ahalf] + al.DECIMAL[:dhalf] + alphabet[ahalf:] + al.DECIMAL[dhalf:] 

	def __encDec(self, text, alphabet=None):
		alphabet = alphabet or al.ENGLISH
		alphabet = self.__createAlphabet(alphabet)
		return self.__rot13.encrypt(text, alphabet=alphabet)

	def encrypt(self, text, key=None, alphabet=None):
		return self.__encDec(text, alphabet)

	def decrypt(self, text, key=None, alphabet=None):
		return self.__encDec(text, alphabet)
