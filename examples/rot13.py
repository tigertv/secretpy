#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import Rot13, CryptMachine, alphabets as al
from secretpy.cmdecorators import SaveAll, Block


def encdec(machine, plaintext):
    print("----------------------------------")
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)


cm = CryptMachine(Rot13())

plaintext = u"The quick brown fox jumps over the lazydog."
encdec(cm, plaintext)

cm = SaveAll(cm)

plaintext = u"Why did the chicken cross the road? Gb trg gb gur bgure fvqr"
encdec(cm, plaintext)

plaintext = u"Die heiße Zypernsonne quälte Max und Victoria ja böse auf dem Weg bis zur Küste."
cm.set_alphabet(al.GERMAN)
encdec(cm, plaintext)

plaintext = u"FAQ om Schweiz: Klöv du trång pjäxby?"
cm.set_alphabet(al.SWEDISH)
encdec(cm, plaintext)

cm.set_alphabet(al.JAPANESE_HIRAGANA)
cm.set_key(1)
plaintext = u"あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをんゃゅょぁぇ"
encdec(cm, plaintext)

cm = Block(cm)
encdec(cm, plaintext)

'''
----------------------------------
The quick brown fox jumps over the lazydog.
gurdhvpxoebjasbkwhzcfbiregurynmlqbt
thequickbrownfoxjumpsoverthelazydog
----------------------------------
Why did the chicken cross the road? Gb trg gb gur bgure fvqr
Jul qvq gur puvpxra pebff gur ebnq? To get to the other side
Why did the chicken cross the road? Gb trg gb gur bgure fvqr
----------------------------------
Die heiße Zypernsonne quälte Max und Victoria ja böse auf dem Weg bis zur Küste.
Sxt wtxot Kjatcüdßüüt bfläet Öpi füs Gxreßcxp yp qmdt pfu stö Htv qxd kfc Zndet.
Die heiße Zypernsonne quälte Max und Victoria ja böse auf dem Weg bis zur Küste.
----------------------------------
FAQ om Schweiz: Klöv du trång pjäxby?
UPB oä Drwhtxk: Zång sf eclöv aymiqj?
FAQ om Schweiz: Klöv du trång pjäxby?
----------------------------------
あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをんゃゅょぁぇ
ねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをんゃゅょぁぇあいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬ
あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをんゃゅょぁぇ
----------------------------------
あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをんゃゅょぁぇ
ねのはひふ へほばびぶ べぼぱぴぷ ぺぽまみむ めもやゆよ らりるれろ わをんゃゅ ょぁぇあい うえおかき くけこがぎ ぐげごさし すせそざじ ずぜぞたち つてとだぢ づでどなに ぬ
あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをんゃゅょぁぇ
'''
