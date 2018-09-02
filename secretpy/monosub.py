#!/usr/bin/python
# -*- encoding: utf-8 -*-

class Monosub:
	def __init__(self):
		return

	def __encDec(self, alphabet, key, text, isEncrypt):
		if len(alphabet) != len(key): return 

		ans = ""
		for i in range(len(text)):
			m = text[i]
			k = ""
			if isEncrypt == 1:
				k = key[alphabet.index(m)]
			else:
				k = alphabet[key.index(m)]
			ans += k
		return ans

	def encrypt(self, alphabet, key, plaintext):
		return self.__encDec(alphabet, key, plaintext, 1)

	def decrypt(self, alphabet, key, ciphertext):
		return self.__encDec(alphabet, key, ciphertext, -1)
