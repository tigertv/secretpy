#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot13, CryptMachine, alphabets as al
from secretpy.cmdecorators import SaveAll


def encdec(machine, plaintext):
    print("----------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)


cm = SaveAll(CryptMachine(Rot13()))

plaintext = u"This is a secret message"
encdec(cm, plaintext)

plaintext = u"Why did the chicken cross the road Gb trg gb gur bgure fvqr"
encdec(cm, plaintext)

plaintext = u"The quick brown fox jumps over the lazydog"
cm.set_alphabet(al.GERMAN)
encdec(cm, plaintext)

plaintext = u"текст"
cm.set_alphabet(al.RUSSIAN)
encdec(cm, plaintext)

cm.set_alphabet(al.JAPANESE_HIRAGANA)
cm.set_key(1)
plaintext = u"あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをんゃゅょぁぇ"
encdec(cm, plaintext)

'''
----------------------------------
This is a secret message
Guvf vf n frperg zrffntr
This is a secret message
----------------------------------
Why did the chicken cross the road Gb trg gb gur bgure fvqr
Jul qvq gur puvpxra pebff gur ebnq To get to the other side
Why did the chicken cross the road Gb trg gb gur bgure fvqr
----------------------------------
The quick brown fox jumps over the lazydog
Ewt bfxrz qcßhü ußi yföad ßgtc ewt äpkjsßv
The quick brown fox jumps over the lazydog
----------------------------------
текст
вхыбв
текст
----------------------------------
あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをんゃゅょぁぇ
ねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをんゃゅょぁぇあいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬ
あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをんゃゅょぁぇ
'''
