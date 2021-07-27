#!/usr/bin/python
# -*- encoding: utf-8 -*-

import math
from collections import OrderedDict
from secretpy import alphabets as al


class PolybiusSquare:
    """
    PolybiusSquare. It's used by many classical ciphers
    """

    def __init__(self, alphabet=al.ENGLISH_SQUARE_IJ, key=None):
        self.__side = int(math.ceil(math.sqrt(len(alphabet))))
        # prepare alphabet for substitution
        if key:
            indexes = {c: i for i, letters in enumerate(alphabet) for c in letters}
            # remove duplicates
            keyi = OrderedDict.fromkeys(indexes[char] for char in key)
            self.__alphabet = [alphabet[i] for i in keyi]

            for i, a in enumerate(alphabet):
                if i not in keyi:
                    self.__alphabet.append(a)
        else:
            self.__alphabet = alphabet
        self.coords = {c: divmod(i, self.__side) for i, letters in enumerate(self.__alphabet) for c in letters}

    def get_coordinates(self, char):
        return self.coords[char]

    def get_char(self, row, column):
        return self.__alphabet[row * self.__side + column][0]

    def get_columns(self):
        return self.__side

    def get_rows(self):
        return len(self.__alphabet) // self.__side
