#!/usr/bin/python
# -*- encoding: utf-8 -*-

from secretpy import ADFGX, CryptMachine, alphabets as al
from secretpy.cmdecorators import SaveAll, Block, UpperCase


alphabet = (
    u"b", u"t", u"a", u"l", u"p",
    u"d", u"h", u"o", u"z", u"k",
    u"q", u"f", u"v", u"s", u"n",
    u"g", u"ij", u"c", u"u", u"x",
    u"m", u"r", u"e", u"w", u"y"
)
key = "cargo"
cipher = ADFGX()
plaintext = u"attackatonce"

print(plaintext)
enc = cipher.encrypt(plaintext, key, alphabet)
print(enc)
print(cipher.decrypt(enc, key, alphabet))
print("----------------------------------")


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    print(machine.decrypt(enc))
    print("----------------------------------")


cm0 = CryptMachine(cipher, key)
cm = UpperCase(Block(cm0))
cm.set_alphabet(alphabet)
plaintext = u"Attack at once!"
encdec(cm, plaintext)

cm1 = SaveAll(cm0)
plaintext = u"Attack at once!"
encdec(cm1, plaintext)

alphabet = al.GERMAN_SQUARE
key = "german"
cm.set_key(key)
cm.set_alphabet(alphabet)
plaintext = u"Schweißgequält vom öden Text zürnt Typograf Jakob"
encdec(cm, plaintext)

alphabet = (
    u"uúů", u"aá", u"b", u"cč", u"dď",
    u"f", u"g", u"h", u"iíj", u"zž",
    u"k", u"l", u"m", u"nň", u"oó",
    u"p", u"q", u"rř", u"sš", u"tť",
    u"v", u"w", u"x", u"yý", u"eéě",
)
key = "czech"
cm.set_key(key)
cm.set_alphabet(alphabet)
plaintext = u"Nechť již hříšné saxofony ďáblů rozezvučí síň úděsnými tóny waltzu, tanga a quickstepu."
encdec(cm, plaintext)

alphabet = (
    u"zž", u"aáä", u"b", u"cč", u"dď",
    u"eé", u"f", u"g", u"h", u"iíj",
    u"k", u"lĺľ", u"m", u"oóô", u"p",
    u"q", u"rŕ", u"sš", u"tť", u"uú",
    u"v", u"w", u"x", u"yý", u"nň",
)
key = "slovak"
cm.set_key(key)
cm.set_alphabet(alphabet)
plaintext = u"Vypätá dcéra grófa Maxwella s IQ nižším ako kôň núti čeľaď hrýzť hŕbu jabĺk."
encdec(cm, plaintext)

alphabet = (
    u"αά", u"β", u"γ", u"δ", u"εέ",
    u"ζ", u"ηή", u"θ", u"ιί", u"κ",
    u"λ", u"μ", u"ν", u"ξ", u"οό",
    u"π", u"ρ", u"σς", u"τ", u"υύ",
    u"φ", u"χ", u"ψ", u"ωώ", u"",
)
key = "greek"
cm.set_key(key)
cm.set_alphabet(alphabet)
plaintext = u"Ξεσκεπάζω την ψυχοφθόρα σας βδελυγμία."
encdec(cm, plaintext)

'''
attackatonce
faxdfadddgdgfffafaxafafx
attackatonce
----------------------------------
Attack at once!
FAXDF ADDDG DGFFF AFAXA FAFX
ATTACKATONCE
----------------------------------
Attack at once!
Faxdfa dd dgdg!fffafaxafafx
Attack at once!
----------------------------------
Schweißgequält vom öden Text zürnt Typograf Jakob
DDAAX FFXGG FGDFF DFAAG GGGDG GAADG XGGFF AGGGG FAAAF XDXGD XXXFG DAXFG XAAGF FXGXD GGAAD GGFAA XFXDD D
SCHWEISGEQUALTVOMODENTEXTZURNTTYPOGRAFIAKOB
----------------------------------
Nechť již hříšné saxofony ďáblů rozezvučí síň úděsnými tóny waltzu, tanga a quickstepu.
FGDXD GAXFX FFXAD GAGFX XDDXD DDAXA XGGGG GFFGA ADXAG AXXGF DGAFD AGGAX FDFGX XAXDA XDAGG XGDXX DADAD AGGAX DFFGF XAFGX XGDAG GGGAX GGAAF XAGDG DGXDD GADFX AGFXF FFGFX ADGGG X
NECHTIIZHRISNESAXOFONYDABLUROZEZVUCISINUDESNYMITONYWALTZUTANGAAQUICKSTEPU
----------------------------------
Vypätá dcéra grófa Maxwella s IQ nižším ako kôň núti čeľaď hrýzť hŕbu jabĺk.
FADDD ADAGA FFXGD AXDGA XDAFD DADAA FGXGA XGGXF ADXDD DFDFX FDAXX DGADX DXGAA FFXFD DDFFG AAGGA AFXAA GGAXF GXGAF XDFDA GDFGG GDGFD DXXXA GXGDD GFDA
VYPATADCERAGROFAMAXWELLASIQNIZSIMAKOKONNUTICELADHRYZTHRBUIABLK
----------------------------------
Ξεσκεπάζω την ψυχοφθόρα σας βδελυγμία.
AXAGF XXXGF AXDXA AGFXA GFAXA GFFGA DFFFA AAAFA GXDGX DDDAD FFAGD AXDGX FAGGG D
ΞΕΣΚΕΠΑΖΩΤΗΝΨΥΧΟΦΘΟΡΑΣΑΣΒΔΕΛΥΓΜΙΑ
----------------------------------
'''
