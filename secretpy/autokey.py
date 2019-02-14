#!/usr/bin/python
# -*- encoding: utf-8 -*-

class Autokey:
	def __init__(self):
		return

	def __encDec(self, alphabet, key, text, isEncrypt):
		ans = ""
		for i in range(len(text)):
			m = text[i]
			if i < len(key):
				k = key[i]
			else:
				if isEncrypt == 1:	
					k = text[i - len(key)]
				else:
					k = ans[i - len(key)]
			alphIndex = (alphabet.index(m) + isEncrypt * alphabet.index(k) ) % len(alphabet)
			enc = alphabet[alphIndex]
			ans += enc
		return ans

	def encrypt(self, key, plaintext, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, key, plaintext, 1)

	def decrypt(self, key, ciphertext, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, key, ciphertext, -1)
