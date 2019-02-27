#!/usr/bin/python

from .rot13 import Rot13
import secretpy.alphabet as al

class Rot5:
	"""
	The Rot5 Cipher
	"""
	__rot13= Rot13()
	__alphabet = al.DECIMAL

	def __encDec(self, text):
		return self.__rot13.encrypt(text, alphabet=self.__alphabet)

	def encrypt(self, text, key=None, alphabet=None):
		"""
		Encryption function

		:param text: Text to encrypt
		:param key: Encryption key
		:param alphabet: Alphabet which will be used, if there is no a value, English is used
		"""
		return self.__encDec(text)

	def decrypt(self, text, key=None, alphabet=None):
		"""
		Decryption function

		:param text: Text to decrypt
		:param key: Decryption key
		:param alphabet: Alphabet which will be used, if there is no a value, English is used
		"""
		return self.__encDec(text)
