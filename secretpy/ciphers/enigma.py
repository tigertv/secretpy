#!/usr/bin/python
# -*- encoding: utf-8 -*-
import secretpy.alphabets as al


class Enigma:
    """
    The Enigma Cipher
    """

    class Rotor:
        def __init__(self, key, alphabet, turnover, position=0, ringsetting=0):
            if isinstance(position, str):
                self.position = alphabet.index(position)
            else:
                self.position = position
            if isinstance(ringsetting, str):
                self.ring = alphabet.index(ringsetting)
            else:
                self.ring = ringsetting
            self.key = key  # the same length as alphabet
            self.alphabet = alphabet
            self.next_rotor = None
            self.turnover = turnover

        def encrypt_char(self, char):
            i = (self.alphabet.index(char) + self.position - self.ring) % len(self.alphabet)
            c = self.key[i]
            i = (self.alphabet.index(c) - self.position + self.ring) % len(self.alphabet)
            return self.alphabet[i]

        def inverse_encrypt(self, char):
            i = (self.alphabet.index(char) + self.position - self.ring) % len(self.alphabet)
            c = self.alphabet[i]
            i = (self.key.index(c) - self.position + self.ring) % len(self.alphabet)
            return self.alphabet[i]

        def rotate(self):
            if self.alphabet[self.position][0] in self.turnover:
                if self.next_rotor:
                    self.next_rotor.rotate()
            self.position += 1
            self.position %= len(self.alphabet)

        def set_next_rotor(self, rotor):
            self.next_rotor = rotor

        def get_position(self):
            return self.alphabet[self.position]

        # end of class Rotor

    def encrypt(self, text, key=None, alphabet=al.ENGLISH):
        """
        Encryption method

        :param text: Text to encrypt
        :param key: Encryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: encrypted text
        :rtype: string
        """
        if not isinstance(key, dict):
            key = {
                'reflector': 'B',
                'rotor_offsets': ('a', 'a', 'a'),  # Grundstellung
                'ring_offsets': ('a', 'a', 'a'),   # Ringstellung
                'rotor_order': (1, 2, 3),
                'steckers': []
            }

        exist_rotors = (
            {'name': 'ENIGMA_I_I', 'wiring': "ekmflgdqvzntowyhxuspaibrcj", 'overturn': 'q'},
            {'name': 'ENIGMA_I_II', 'wiring': "ajdksiruxblhwtmcqgznpyfvoe", 'overturn': 'e'},
            {'name': 'ENIGMA_I_III', 'wiring': "bdfhjlcprtxvznyeiwgakmusqo", 'overturn': 'v'},
            {'name': 'M3_ARMY_IV', 'wiring': "esovpzjayquirhxlnftgkdcmwb", 'overturn': 'j'},
            {'name': 'M3_ARMY_V', 'wiring': "vzbrgityupsdnhlxawmjqofeck", 'overturn': 'z'},
            {'name': 'M3_M4_NAVAL_VI', 'wiring': "jpgvoumfyqbenhzrdkasxlictw", 'overturn': 'zm'},
            {'name': 'M3_M4_NAVAL_VII', 'wiring': "nzjhgrcxmyswboufaivlpekqdt", 'overturn': 'zm'},
            {'name': 'M3_M4_NAVAL_VIII', 'wiring': "fkqhtlxocbjspdzramewniuygv", 'overturn': 'zm'},
        )

        exist_reflectors = {
            'A': "ejmzalyxvbwfcrquontspikhgd",
            'B': "yruhqsldpxngokmiebfzcwvjat",
            'C': "fvpjiaoyedrzxwgctkuqsbnmhl",
        }

        plugboard = {c: c for c in alphabet}
        for s1, s2 in key['steckers']:
            plugboard[s1] = s2
            plugboard[s2] = s1

        # set reflector, it behaves as a rotor without rotation
        rotors = [self.Rotor(exist_reflectors[key['reflector']], alphabet, 0, 0, 0)]

        # set other rotors
        for i, ri in enumerate(key['rotor_order']):
            r = exist_rotors[ri - 1]
            rotor = self.Rotor(r['wiring'], alphabet, r['overturn'], key['rotor_offsets'][i], key['ring_offsets'][i])
            rotors.append(rotor)

        # connect rotors
        for i in range(len(rotors) - 1, 1, -1):
            rotors[i].set_next_rotor(rotors[i - 1])

        res = []
        for c in text:
            # rotate before send a char
            rotors[-1].rotate()
            c = plugboard[c]
            # we go from right to left
            for r in reversed(rotors):
                c = r.encrypt_char(c)
            it = iter(rotors)
            next(it)  # omit reflector
            # and then go back
            for r in it:
                c = r.inverse_encrypt(c)
            c = plugboard[c]
            res.append(c)
        return "".join(res)

    def decrypt(self, text, key=None, alphabet=al.ENGLISH):
        """
        Decryption method

        :param text: Text to decrypt
        :param key: Decryption key
        :param alphabet: Alphabet which will be used,
                         if there is no a value, English is used
        :type text: string
        :type key: integer
        :type alphabet: string
        :return: decrypted text
        :rtype: string
        """
        return self.encrypt(text, key, alphabet)
