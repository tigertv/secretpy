#!/usr/bin/python

class Rot13:
	def __init__(self):
		return
	
	def __encDec(self, alphabet, key, text, isEncrypt):
		ans = ""
		for char in text:
			alphIndex = (alphabet.index(char) + isEncrypt * key) % len(alphabet)
			ans += alphabet[alphIndex]
		return ans

	def encrypt(self, key, plaintext, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		key = len(alphabet) / 2
		return self.__encDec(alphabet, key, plaintext, 1)

	def decrypt(self, key, ciphertext, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		key = len(alphabet) / 2
		return self.__encDec(alphabet, key, ciphertext, -1)
