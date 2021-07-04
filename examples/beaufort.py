#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Beaufort, CryptMachine, alphabets as al
from secretpy.cmdecorators import SaveAll, RemoveNonAlphabet


def encdec(cipher, plaintext, key, alphabet=al.ENGLISH):
    print('========================================================================================')
    print(plaintext)
    enc = cipher.encrypt(plaintext, key, alphabet)
    print(enc)
    print(cipher.decrypt(enc, key, alphabet))


key = "key"
cipher = Beaufort()

plaintext = u"thequickbrownfoxjumpsoverthelazydog"
encdec(cipher, plaintext, key)

alphabet = al.GERMAN
plaintext = u"schweißgequältvomödentextzürnttypografjakob"
encdec(cipher, plaintext, key, alphabet)

alphabet = al.SWEDISH
plaintext = u"faqomschweizklövdutrångpjäxby"
encdec(cipher, plaintext, key, alphabet)

# using cryptmachine


def encdec(machine, plaintext):
    print("--------------------------------------------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))


cm0 = CryptMachine(cipher, key)

plaintext = "I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!"
cm = SaveAll(cm0)
encdec(cm, plaintext)

cm.set_alphabet(al.ENGLISH_SQUARE_IJ)
plaintext = "Jj becomes Ii because we use ENGLISH_SQUARE_IJ!"
encdec(cm, plaintext)

cm.set_alphabet(al.JAPANESE_HIRAGANA)
cm.set_key(u"だやぎへ")
plaintext = u"text あい だやぎへぐゆぢ"
encdec(cm, plaintext)

plaintext = "I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!"
cm = RemoveNonAlphabet(cm0)
cm.set_alphabet(al.ENGLISH)
cm.set_key(key)
encdec(cm, plaintext)

'''
Output:

========================================================================================
thequickbrownfoxjumpsoverthelazydog
rxuukqiuxtqcxzknveypgwjutlrgtylgvwy
thequickbrownfoxjumpsoverthelazydog
========================================================================================
schweißgequältvomödentextzürnttypografjakob
wcrsaqlüuyoüßpdäwöhalvabvjäxvfvkjäühkßpkykj
schweißgequältvomödentextzürnttypografjakob
========================================================================================
faqomschweizklövdutrångpjäxby
feizvgiåcgzöawzsbeuqäåäjbgbjj
faqomschweizklövdutrångpjäxby
--------------------------------------------------------------------
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
C tkpa lwr-yzprkdur crknyilutm. Fdagg ehg : ^,&@$~(*;?&#. Lrkl'g cl!
I love non-alphabet characters. These are : ^,&@$~(*;?&#. That's it!
--------------------------------------------------------------------
Jj becomes Ii because we use ENGLISH_SQUARE_IJ!
Bw xfclyag Bw xfcyqnu oa esa UXYOBNR_SPEKOU_BW!
Ii becomes Ii because we use ENGLISH_SQUARE_II!
--------------------------------------------------------------------
text あい だやぎへぐゆぢ
text だも むもそすぇめぇ
text あい だやぎへぐゆぢ
--------------------------------------------------------------------
I don't love non-alphabet characters. I will remove all of them: ^,&@$~(*;?&#. Great!
cbkxlnwjuxqlktjdexglwdehkcfgngciqzthgskpayztkflrgsstayr
idontlovenonalphabetcharactersiwillremoveallofthemgreat
'''
