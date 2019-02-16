#!/usr/bin/python
	
class Atbash:
	def __init__(self):
		return
	
	def __encDec(self, alphabet, text):
		ans = ""
		for char in text:
			alphIndex = len(alphabet) - (alphabet.index(char)) - 1 
			enc = alphabet[alphIndex]
			ans += enc
		return ans

	def encrypt(self, text, key=None, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, text)

	def decrypt(self, text, key=None, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, text)
