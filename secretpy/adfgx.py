#!/usr/bin/python
# -*- encoding: utf-8 -*-
from __future__ import division
import sys
import math

class ADFGX:
	header = u"adfgx"

	def __init__(self):
		return

	def __dec(self, alphabet, key, text, isEncrypt):
		keysize = len(key)
		side = int(math.ceil(math.sqrt(len(alphabet))))
		size = len(text)
		rows = int(math.ceil(size/keysize))
		reminder = size % keysize
		keyword = list(key)
		indices = sorted(range(len(keyword)), key=lambda k: keyword[k])

		myarr = list(indices)
		lefti = 0
		righti = 0
		for key, value in enumerate(indices):
			righti = lefti
			righti += rows
			if reminder > 0 and value > reminder-1: righti -= 1
			myarr[value] = text[lefti:righti]
			lefti = righti

		column = 0
		row = 0
		res = ''
		for i in range(size):
			res += (myarr[column][row])
			column += 1
			if column == keysize: 
				column = 0
				row += 1

		# now get resulting symbols from alphabet and the res variable
		dec = ""
		for i in range(size >> 1):
			row = self.header.index(res[i*2])
			column = self.header.index(res[i*2+1])
			index = row*side + column
			dec += alphabet[index][0]

		return dec

	def __enc(self, alphabet, key, text, isEncrypt):
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
	
	def encrypt(self, text, key, alphabet=None):
		alphabet = alphabet or [u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"ij", u"k", u"l", u"m", u"n", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z"]
		return self.__enc(alphabet, key, text, 1)

	def decrypt(self, text, key, alphabet=None):
		alphabet = alphabet or [u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"ij", u"k", u"l", u"m", u"n", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z"]
		return self.__dec(alphabet, key, text, -1)
