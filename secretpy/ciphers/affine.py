#!/usr/bin/python


class Affine:
    """
    The Affine Cipher
    """

    def __crypt(self, alphabet, key, text, is_encrypt):
        a = key[0]
        b = key[1]
        res = []
        a_inverse = self.__get_inverse(a, alphabet)
        try:
            for char in text:
                if is_encrypt == 1:
                    a_index = (alphabet.index(char) * a + b) % len(alphabet)
                else:
                    a_index = (a_inverse * (alphabet.index(char) - b)) % len(alphabet)
                enc = alphabet[a_index]
                res.append(enc)
        except ValueError:
            wrchar = char.encode('utf-8')
            raise Exception("Can't find char '" + wrchar + "' of text in alphabet!")
        return "".join(res)

    def __get_inverse(self, a, alphabet):
        for i in range(1, len(alphabet)):
            if ((int(a)*int(i)) % int(len(alphabet))) == 1:
                return i
        return 0

    def encrypt(self, text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return self.__crypt(alphabet, key, text, 1)

    def decrypt(self, text, key, alphabet=u"abcdefghijklmnopqrstuvwxyz"):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used, if there is no a value,
                         English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: text
        :rtype: string
        """
        return self.__crypt(alphabet, key, text, -1)
