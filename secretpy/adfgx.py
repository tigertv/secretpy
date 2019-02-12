#!/usr/bin/python
# -*- encoding: utf-8 -*-
from __future__ import division
import sys
import math

class ADFGX:
	header = u"adfgx"

	def __init__(self):
		return

	def __encDec(self, alphabet, key, text, isEncrypt):
		ans0 = ""
		size = int(math.ceil(math.sqrt(len(alphabet))))
		for i in range(len(text)):
			char = text[i]
			for j in range(len(alphabet)):
				try:
					alphabet[j].index(char)
					break
				except:
					pass
			row = int(j/size)
			column  = j % size
			ans0 += self.header[row] + self.header[column]
		
		ans = list(ans0)
		keyword = list(key)
		keysize = len(key)
		size = len(ans)
		indices = sorted(range(len(keyword)), key=lambda k: keyword[k])
		row = int(math.ceil(size/keysize))
		for i in range(row):
			p = ""
			for j in range(keysize):
				myi = i*keysize+j
				if myi < len(ans):
					eee = ans[myi]
					p += "".join(eee)

		ans2 = ""
		for s in indices:
			ind = s
			while ind < size:
				p = ans[ind]
				ans2 += p
				ind += keysize
		
		return ans2
	
	def encrypt(self, alphabet, key, plaintext):
		return self.__encDec(alphabet, key, plaintext, 1)

	def decrypt(self, alphabet, key, ciphertext):
		#return "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
		return self.__encDec(alphabet, key, ciphertext, -1)
