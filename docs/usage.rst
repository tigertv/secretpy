Usage
=====

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

In the previous example plaintext contains only letters existing in the alphabet and in the lower case without spaces.
To change the behaviour you can use CryptMachine and decorators(UpperCase, NoSpace, SaveCase and etc.):

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

Combining several ciphers to get more complex cipher, you can use CompositeMachine:

.. code-block:: python

	#!/usr/bin/python
	# -*- encoding: utf-8 -*-

	from secretpy import Rot13
	from secretpy import Caesar
	from secretpy import CryptMachine
	from secretpy import CompositeMachine
	from secretpy.cmdecorators import *

	def encdec(machine, plaintext):
		print("=======================================")
		print(plaintext)
		enc = machine.encrypt(plaintext)
		print(enc)
		dec = machine.decrypt(enc)
		print(dec)

	key = 5
	plaintext = u"Dog jumps four times and cat six times"
	print(plaintext)

	cm1 = SaveSpaces(SaveCase(CryptMachine(Caesar(), key)))
	enc = cm1.encrypt(plaintext)
	print(enc)

	cm2 = SaveSpaces(SaveCase(CryptMachine(Rot13())))
	enc = cm2.encrypt(enc)
	print(enc)

	print("=======================================")

	cm = CompositeMachine(cm1)
	cm.addMachines(cm2)
	enc = cm.encrypt(plaintext)
	print(enc)

	encdec(cm, plaintext)

	cm.addMachines(cm1, cm2)
	encdec(cm, plaintext)

	'''
	Output:
	
	Dog jumps four times and cat six times
	Itl ozrux ktzw ynrjx fsi hfy xnc ynrjx
	Vgy bmehk xgmj laewk sfv usl kap laewk
	=======================================
	Vgy bmehk xgmj laewk sfv usl kap laewk
	=======================================
	Dog jumps four times and cat six times
	Vgy bmehk xgmj laewk sfv usl kap laewk
	Dog jumps four times and cat six times
	=======================================
	Dog jumps four times and cat six times
	Nyq tewzc pyeb dswoc kxn mkd csh dswoc
	Dog jumps four times and cat six times
	'''
