#!/usr/bin/python
# -*- encoding: utf-8 -*-
from collections import OrderedDict

class Keyword:
	def __init__(self):
		return

	def __removeDup(self, input_str):
		newstring = input_str[0]
		for i in xrange(len(input_str)):
			if newstring[(len(newstring) - 1 )] != input_str[i]:
				newstring += input_str[i]
			else:
				pass
		return newstring

	def __encDec(self, alphabet, key, text, isEncrypt):
		#remove repeats of letters in the key 
		newkey = "".join(OrderedDict.fromkeys(key))
		#create the substitution string
		longkey = "".join(OrderedDict.fromkeys(newkey+"".join(alphabet)))
		#do encryption
		ans = ""
		for i in range(len(text)):
			m = text[i]
			if isEncrypt == 1:
				index = alphabet.index(m)
				enc = longkey[index]
			else:
				index = longkey.index(m)
				enc = alphabet[index]
			ans += enc
		return ans

	def encrypt(self, text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, key, text, 1)

	def decrypt(self, text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(alphabet, key, text, -1)
