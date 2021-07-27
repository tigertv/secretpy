========
SecretPy
========

|PyPIpkg| |PythonV| |PythonImplement| |Docs| |Downloads| |License| |Travis|

**Download:**

https://pypi.org/project/secretpy

**Documentation:**

https://secretpy.readthedocs.io

**Source code & Development:**

https://github.com/tigertv/secretpy

Description
===========

SecretPy is a cryptographic Python package. It uses the following classical cipher algorithms:

* Affine
* Atbash
* Bazeries
* Beaufort
* Caesar, Caesar Progressive
* Chaocipher
* Keyword
* Playfair, Two Square(Double Playfair), Three Square, Four Square
* Polybius, ADFGX, ADFGVX, Bifid, Trifid, Nihilist
* Rot13, Rot5, Rot18, Rot47
* Simple Substitution
* Transposition: Columnar, Scytale, Spiral, Myszkowski, Zigzag(Railfence)
* Vic
* Vigenere, Autokey, Gronsfeld, Porta

Installation
============

To install this library, you can use pip:

.. code-block:: bash

	pip install secretpy

Alternatively, you can install the package using the repo's cloning and the make:

.. code-block:: bash

	git clone https://github.com/tigertv/secretpy
	cd secretpy
	make install

Usage
=====

Direct way
----------

The cipher classes can encrypt only characters which exist in the alphabet, and they don't have a state.

.. code-block:: python
	
	from secretpy import Caesar, alphabets as al


	def encdec(cipher, plaintext, key, alphabet=al.ENGLISH):
	    print('========================================================================================')
	    print(plaintext)
	    enc = cipher.encrypt(plaintext, key, alphabet)
	    print(enc)
	    print(cipher.decrypt(enc, key, alphabet))


	key = 3
	cipher = Caesar()

	plaintext = u"thequickbrownfoxjumpsoverthelazydog"
	encdec(cipher, plaintext, key)

	alphabet = al.GERMAN
	plaintext = u"schweißgequältvomödentextzürnttypografjakob"
	encdec(cipher, plaintext, key, alphabet)

	alphabet = al.SWEDISH
	plaintext = u"faqomschweizklövdutrångpjäxby"
	encdec(cipher, plaintext, key, alphabet)

	'''
	Output:

	========================================================================================
	thequickbrownfoxjumpsoverthelazydog
	wkhtxlfneurzqiramxpsvryhuwkhodcbgrj
	thequickbrownfoxjumpsoverthelazydog
	========================================================================================
	schweißgequältvomödentextzürnttypografjakob
	vfkzhlcjhtxßowyrpaghqwhäwübuqwwösrjudimdnre
	schweißgequältvomödentextzürnttypografjakob
	========================================================================================
	faqomschweizklövdutrångpjäxby
	idtrpvfkzhlönocygxwuaqjsmbåeä
	faqomschweizklövdutrångpjäxby
	'''

CryptMachine
------------

``CryptMachine`` saves a state. There are alphabet, key and cipher, they can be changed at anytime.
In the previous example, plaintext contains only characters existing in the alphabet i.e. without spaces and etc.
To change the behaviour, you can use ``CryptMachine`` and decorators(``SaveAll``, ``Block``), so it's a preferred way to do encryption/decryption:

.. code-block:: python
	
	from secretpy import Caesar, CryptMachine, alphabets as al
	from secretpy.cmdecorators import SaveAll, Block


	def encdec(machine, plaintext):
	    print("--------------------------------------------------------------------")
	    print(plaintext)
	    enc = machine.encrypt(plaintext)
	    print(enc)
	    print(machine.decrypt(enc))


	key = 3
	cipher = Caesar()
	cm0 = CryptMachine(cipher, key)

	cm = cm0
	cm.set_alphabet(al.ENGLISH)
	plaintext = "I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!"
	encdec(cm, plaintext)

	cm = Block(cm, length=5, sep="-")
	plaintext = "This text is divided by blocks of length 5!"
	encdec(cm, plaintext)

	cm = SaveAll(cm0)
	plaintext = "I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!"
	encdec(cm, plaintext)

	cm.set_alphabet(al.ENGLISH_SQUARE_IJ)
	plaintext = "Jj becomes Ii because we use ENGLISH_SQUARE_IJ!"
	encdec(cm, plaintext)

	cm.set_alphabet(al.JAPANESE_HIRAGANA)
	cm.set_key(1)
	plaintext = u"text あい だやぎへぐゆぢ"
	encdec(cm, plaintext)

	'''
	Output:

	--------------------------------------------------------------------
	I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!
	lgrqworyhqrqdoskdehwfkdudfwhuvlzloouhpryhdooriwkhpjuhdw
	idontlovenonalphabetcharactersiwillremoveallofthemgreat
	--------------------------------------------------------------------
	This text is divided by blocks of length 5!
	wklvw-hawlv-glylg-hgebe-orfnv-riohq-jwk
	thistextisdividedbyblocksoflength
	--------------------------------------------------------------------
	I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
	L oryh qrq-doskdehw fkdudfwhuv. Wkhvh duh : ^,&@$~(*;?&#. Wkdw'v lw!
	I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
	--------------------------------------------------------------------
	Jj becomes Ii because we use ENGLISH_SQUARE_IJ!
	Mm ehfrphv Mm ehfdxvh zh xvh HQKOMVL_VTXDUH_MM!
	Ii becomes Ii because we use ENGLISH_SQUARE_II!
	--------------------------------------------------------------------
	text あい だやぎへぐゆぢ
	text いう ぢゆぐほげよづ
	text あい だやぎへぐゆぢ
	'''

CompositeMachine
----------------

Combining several ciphers to get more complex cipher, you can use ``CompositeMachine``:

.. code-block:: python

	from secretpy import Rot13, Caesar, CryptMachine, CompositeMachine
	from secretpy.cmdecorators import SaveAll


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

	cm1 = SaveAll(CryptMachine(Caesar(), key))
	enc = cm1.encrypt(plaintext)
	print(enc)

	cm2 = SaveAll(CryptMachine(Rot13()))
	enc = cm2.encrypt(enc)
	print(enc)

	print("=======================================")

	cm = CompositeMachine(cm1)
	cm.add_machines(cm2)
	enc = cm.encrypt(plaintext)
	print(enc)
	encdec(cm, plaintext)

	cm.add_machines(cm1, cm2)
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

Maintainers
===========

- `@tigertv <https://github.com/tigertv>`_ (Max Vetrov)

.. Images and Links 

.. |PyPIpkg| image:: https://img.shields.io/pypi/v/secretpy.svg?style=flat-square
	:alt: Go to PyPi
	:target: https://pypi.org/project/secretpy
.. |PythonV| image:: https://img.shields.io/pypi/pyversions/secretpy.svg?style=flat-square
	:alt: Go to PyPi
	:target: https://pypi.org/project/secretpy
.. |PythonImplement| image:: https://img.shields.io/pypi/implementation/secretpy.svg?style=flat-square
	:alt: Go to PyPi
	:target: https://pypi.org/project/secretpy
.. |Docs| image:: https://img.shields.io/readthedocs/secretpy.svg?style=flat-square
	:alt: Read the Docs
	:target: https://secretpy.readthedocs.io/en/latest
.. |Downloads| image:: https://img.shields.io/pypi/dm/secretpy.svg?style=flat-square
	:alt: Go to PyPi
	:target: https://pypi.org/project/secretpy
.. |License| image:: https://img.shields.io/github/license/tigertv/secretpy.svg?style=flat-square
	:alt: Go to Github
	:target: https://github.com/tigertv/secretpy
.. |Travis| image:: https://img.shields.io/travis/tigertv/secretpy/master.svg?style=flat-square
	:alt: Go to Travis
	:target: https://travis-ci.org/tigertv/secretpy

