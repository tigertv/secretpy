#!/usr/bin/python
# -*- encoding: utf-8 -*-

class Caesar:
	def __init__(self):
		return
	
	def __encDec(self, alphabet, key, text, isEncrypt):
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

	def encrypt(self, text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, key, text, 1)

	def decrypt(self, text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, key, text, -1)
