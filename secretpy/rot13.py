#!/usr/bin/python

class Rot13:
	def __init__(self):
		return
	
	def __encDec(self, alphabet, text, isEncrypt):
		key = len(alphabet) / 2
		ans = ""
		for char in text:
			alphIndex = (alphabet.index(char) + isEncrypt * key) % len(alphabet)
			ans += alphabet[alphIndex]
		return ans

	def encrypt(self, text, key=None, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, text, 1)

	def decrypt(self, text, key=None, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, text, -1)
