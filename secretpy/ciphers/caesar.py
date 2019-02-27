#!/usr/bin/python
# -*- encoding: utf-8 -*-

import secretpy.alphabet as al

class Caesar:
	"""
	The Caesar Cipher
	"""
	__alphabet = al.ENGLISH
	
	def __encDec(self, alphabet, key, text, isEncrypt):
		alphabet = alphabet or self.__alphabet
		ans = ""
		for char in text:
			try:
				alphIndex = alphabet.index(char)
			except ValueError as e:
				e.args = ("Can't find char '" + char.encode('utf-8') + "' of text in alphabet!",)
				raise 
			alphIndex = (alphIndex + isEncrypt * key) % len(alphabet)
			ans += alphabet[alphIndex]
		return ans

	def encrypt(self, text, key, alphabet=None):
		"""
		Encryption function

		:param text: Text to encrypt
		:param key: Encryption key
		:param alphabet: Alphabet which will be used, if there is no a value, English is used
		"""
		return self.__encDec(alphabet, key, text, 1)

	def decrypt(self, text, key, alphabet=None):
		"""
		Decryption function

		:param text: Text to decrypt
		:param key: Decryption key
		:param alphabet: Alphabet which will be used, if there is no a value, English is used
		"""
		return self.__encDec(alphabet, key, text, -1)
