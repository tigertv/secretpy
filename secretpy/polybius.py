#!/usr/bin/python
# -*- encoding: utf-8 -*-
import sys
import math

class Polybius:
	def __init__(self):
		return

	def __encDec(self, alphabet, key, text, isEncrypt):
		ans = ""
		size = int(math.ceil(math.sqrt(len(alphabet))))
		for i in range(len(text)):
			char = text[i]

			for j in range(len(alphabet)):
				try:
					alphabet[j].index(char)
					break
				except:
					pass

			alphIndex = (j + isEncrypt * size ) % len(alphabet)
			ans += alphabet[alphIndex][0]
		return ans

	def encrypt(self, alphabet, key, plaintext):
		return self.__encDec(alphabet, key, plaintext, 1)

	def decrypt(self, alphabet, key, ciphertext):
		return self.__encDec(alphabet, key, ciphertext, -1)
