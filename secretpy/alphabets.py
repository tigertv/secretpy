#!/usr/bin/python
# -*- encoding: utf-8 -*-


BINARY = u"01"
DECIMAL = u"0123456789"
DOZENAL = u"0123456789ab"
HEX = u"0123456789abcdef"
OCTAL = u"01234567"

ARABIC = u"غظضذخثتشرقصفعسنملكيطحزوهدجبأ"
CZECH = u"aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž"
DANISH = u"abcdefghijklmnopqrstuvwxyzæøå"
DUTCH = u"abcdefghijklmnopqrstuvwxyz"
ENGLISH = u"abcdefghijklmnopqrstuvwxyz"
GERMAN = u"abcdefghijklmnopqrstuvwxyzäöüß"
GREEK = u"αάβγδεέζηήθιίκλμνξοόπρσςτυύφχψωώ"
HEBREW = u"אבגדהוזחטיךכלםמןנסעףפץצקרשת"
ICELANDIC = u"aábdðeéfghiíjklmnoóprstuúvxyýþæö"
ITALIAN = u"abcdefghilmnopqrstuvz"
NORWEGIAN = DANISH
POLISH = u"aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
RUSSIAN = u"абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
SLOVAK = u"aáäbcčdďeéfghiíjklĺľmnňoóôpqrŕsštťuúvwxyýzž"
SPANISH = u"abcdefghijklmnñopqrstuvwxyz"
SWEDISH = u"abcdefghijklmnopqrstuvwxyzåäö"
TURKISH = u"abcçdefgğhıijklmnoöprsştuüvyz"

CZECH_SQUARE = (
    u"aá", u"b", u"cč", u"dď", u"eéě",
    u"f", u"g", u"h", u"iíj", u"k",
    u"l", u"m", u"nň", u"oó", u"p",
    u"q", u"rř", u"sš", u"tť", u"uúů",
    u"v", u"w", u"x", u"yý", u"zž",
)

ENGLISH_SQUARE_IJ = (
    u"a", u"b", u"c", u"d", u"e",
    u"f", u"g", u"h", u"ij", u"k",
    u"l", u"m", u"n", u"o", u"p",
    u"q", u"r", u"s", u"t", u"u",
    u"v", u"w", u"x", u"y", u"z",
)

ENGLISH_SQUARE_OQ = (
    u"a", u"b", u"c", u"d", u"e",
    u"f", u"g", u"h", u"i", u"j",
    u"k", u"l", u"m", u"n", u"oq",
    u"p", u"r", u"s", u"t", u"u",
    u"v", u"w", u"x", u"y", u"z",
)

ENGLISH_SQUARE_NO_Z = (
    u"a", u"b", u"c", u"d", u"e",
    u"f", u"g", u"h", u"i", u"j",
    u"k", u"l", u"m", u"n", u"o",
    u"p", u"q", u"r", u"s", u"t",
    u"u", u"v", u"w", u"x", u"y",
)

GERMAN_SQUARE = (
    u"aä", u"b", u"c", u"d", u"e",
    u"f", u"g", u"h", u"ij", u"k",
    u"l", u"m", u"n", u"oö", u"p",
    u"q", u"r", u"sß", u"t", u"uü",
    u"v", u"w", u"x", u"y", u"z"
)

GREEK_SQUARE = (
    u"αά", u"β", u"γ", u"δ", u"εέ",
    u"ζ", u"ηή", u"θ", u"ιί", u"κ",
    u"λ", u"μ", u"ν", u"ξ", u"οό",
    u"π", u"ρ", u"σ", u"ς", u"τ",
    u"υύ", u"φ", u"χ", u"ψ", u"ωώ"
)

RUSSIAN_SQUARE = (
    u"а", u"б", u"в", u"г", u"д", u"её",
    u"ж", u"з", u"ий", u"к", u"л", u"м",
    u"н", u"о", u"п", u"р", u"с", u"т",
    u"у", u"ф", u"х", u"ц", u"ч", u"ш",
    u"щ", u"ы", u"ьъ", u"э", u"ю", u"я",
    u"0", u"1", u"2", u"3", u"4", u"5"
)

SLOVAK_SQUARE = (
    u"aáä", u"b", u"cč", u"dď", u"eé",
    u"f", u"g", u"h", u"iíj", u"k",
    u"lĺľ", u"m", u"nň", u"oóô", u"p",
    u"q", u"rŕ", u"sš", u"tť", u"uú",
    u"v", u"w", u"x", u"yý", u"zž",
)

SPANISH_SQUARE = (
    u"a", u"b", u"c", u"d", u"e",
    u"f", u"g", u"h", u"ij", u"k",
    u"l", u"m", u"nñ", u"o", u"p",
    u"q", u"r", u"s", u"t", u"u",
    u"v", u"w", u"x", u"y", u"z"
)

JAPANESE_HIRAGANA = (
    u"あいうえお"
    u"かきくけこ"
    u"がぎぐげご"
    u"さしすせそ"
    u"ざじずぜぞ"
    u"たちつてと"
    u"だぢづでど"
    u"なにぬねの"
    u"はひふへほ"
    u"ばびぶべぼ"
    u"ぱぴぷぺぽ"
    u"まみむめも"
    u"やゆよ"
    u"らりるれろ"
    u"わを"
    u"ん"
    u"ゃゅょぁぇ"
)
