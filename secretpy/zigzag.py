#!/usr/bin/python
# -*- encoding: utf-8 -*-

class Zigzag:
	def __init__(self):
		return
	# traspositional cipher, no need an alphabet
	def __encDec(self, key, text, isEncrypt):
		ans = ""
		j = 0
		if isEncrypt == -1:
			ans = "." * len(text)
			ans = list(ans)

		shift1 = key << 1
		shift2 = -2
		isPlusShift1 = True

		for row in range(key):
			shift1 -= 2
			shift2 += 2
			i = row
			while i < len(text):
				if isEncrypt == 1:
					ans += text[i]
				else:
					ans[i] = text[j]
					j += 1
				if isPlusShift1:
					if shift1 == 0:
						i += shift2
					else:
						i += shift1
					isPlusShift1 = False
				else:
					if shift2 == 0:
						i += shift1
					else:
						i += shift2
					isPlusShift1 = True

		if isEncrypt == -1:
			ans = "".join(ans)
		return ans

	def encrypt(self, key, plaintext, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(key, plaintext, 1)

	def decrypt(self, key, ciphertext, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
		return self.__encDec(key, ciphertext, -1)
