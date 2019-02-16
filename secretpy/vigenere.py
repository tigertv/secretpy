#!/usr/bin/python
# -*- encoding: utf-8 -*-

class Vigenere:
	def __init__(self):
		return

	def __encDec(self, alphabet, key, text, isEncrypt):
		ans = ""
		for i in range(len(text)):
			char = text[i]
			keychar = key[i % len(key)]
			alphIndex = (alphabet.index(char) + isEncrypt * alphabet.index(keychar) ) % len(alphabet)
			ans += alphabet[alphIndex]
		return ans

	def encrypt(self, key, plaintext, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, key, plaintext, 1)

	def decrypt(self, key, ciphertext, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, key, ciphertext, -1)
