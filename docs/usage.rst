Usage
-----

.. code-block:: python

	#!/usr/bin/python
	# -*- encoding: utf-8 -*-

	from secretpy import Caesar
	from secretpy import alphabet

	alphabet = alphabet.GERMAN
	plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
	key = 3
	cipher = Caesar()

	print(plaintext)
	enc = cipher.encrypt(plaintext, key, alphabet)
	print(enc)
	dec = cipher.decrypt(enc, key, alphabet)
	print(dec)

	print('=====================================')

	print(plaintext)
	# use default english alphabet
	enc = cipher.encrypt(plaintext, key)
	print(enc)
	dec = cipher.decrypt(enc, key)
	print(dec)

	'''
	Output:

	thequickbrownfoxjumpsoverthelazydog
	wkhtxlfneurzqirämxpsvryhuwkhodüögrj
	thequickbrownfoxjumpsoverthelazydog
	=====================================
	thequickbrownfoxjumpsoverthelazydog
	wkhtxlfneurzqiramxpsvryhuwkhodcbgrj
	thequickbrownfoxjumpsoverthelazydog
	'''

You can use CryptMachine and decorators for that:

.. code-block:: python

	#!/usr/bin/python
	# -*- encoding: utf-8 -*-

	from secretpy import Atbash 
	from secretpy import Caesar

	from secretpy import CryptMachine 
	from secretpy.cmdecorators import *
	from secretpy import alphabet

	def encdec(machine, plaintext):
		print(plaintext)
		enc = machine.encrypt(plaintext)
		print(enc)
		dec = machine.decrypt(enc)
		print(dec)
		print("-----------------------------------")

	plaintext  = u"thequickbrownfoxjumpsoverthelazydog"
	key = 3
	cipher = Caesar()

	cm = CryptMachine(cipher, key)
	encdec(cm, plaintext)

	cm.setAlphabet(alphabet.GERMAN)
	encdec(cm, plaintext)

	cm = SaveSpaces(cm)
	cm.setKey(9)
	plaintext  = u"the quick brown fox jumps over the lazy dog"
	encdec(cm, plaintext)

	cm = NoSpaces(UpperCase(cm))
	cm.setCipher(Atbash())
	plaintext  = u"Achtung Minen"
	encdec(cm, plaintext)

	'''
	Output:

	thequickbrownfoxjumpsoverthelazydog
	wkhtxlfneurzqiramxpsvryhuwkhodcbgrj
	thequickbrownfoxjumpsoverthelazydog
	-----------------------------------
	thequickbrownfoxjumpsoverthelazydog
	wkhtxlfneurzqirämxpsvryhuwkhodüögrj
	thequickbrownfoxjumpsoverthelazydog
	-----------------------------------
	the quick brown fox jumps over the lazy dog
	üqn zßrlt käxbw oxc sßvyö xanä üqn ujed mxp
	the quick brown fox jumps over the lazy dog
	-----------------------------------
	Achtung Minen
	ßÖWKJQXRVQZQ
	ACHTUNGMINEN
	-----------------------------------
	'''
