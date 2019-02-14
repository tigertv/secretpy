#!/usr/bin/python
	
class Atbash:
	def __init__(self):
		return
	
	def __encDec(self, alphabet, key, text, isEncrypt):
		ans = ""
		for char in text:
			alphIndex = len(alphabet) - (alphabet.index(char)) - 1 
			enc = alphabet[alphIndex]
			ans += enc
		return ans

	def encrypt(self, key, plaintext, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, key, plaintext, 1)

	def decrypt(self, key, ciphertext, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, key, ciphertext, -1)
