#!/usr/bin/python
# -*- encoding: utf-8 -*-

class Beaufort:
	def __init__(self):
		return

	def __encDec(self, alphabet, key, text):
		ans = ""
		for i in range(len(text)):
			char = text[i]
			keychar = key[i % len(key)]
			alphIndex = (alphabet.index(keychar) - alphabet.index(char)) % len(alphabet)
			ans += alphabet[alphIndex]
		return ans

	def encrypt(self, text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, key, text)

	def decrypt(self, text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, key, text)
