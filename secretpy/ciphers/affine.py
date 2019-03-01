#!/usr/bin/python


class Affine:
    """
    The Affine Cipher
    """

    def __encDec(self, alphabet, key, text, isEncrypt):
        a = key[0]
        b = key[1]
        ans = ""
        aInverse = self.__getInverse(a, alphabet)
        for char in text:
            if isEncrypt == 1:
                alphI = (alphabet.index(char) * a + b) % len(alphabet)
            else:
                alphI = (aInverse * (alphabet.index(char) - b)) % len(alphabet)
            enc = alphabet[alphI]
            ans += enc
        return ans

    def __getInverse(self, a, alphabet):
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
        return self.__encDec(alphabet, key, text, 1)

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
        return self.__encDec(alphabet, key, text, -1)
