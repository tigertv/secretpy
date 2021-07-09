#!/usr/bin/python
# -*- encoding: utf-8 -*-

import math
from collections import OrderedDict
from secretpy import alphabets as al


class PolybiusSquare:
    """
    PolybiusSquare. It's used by many classical ciphers
    """

    def __init__(self, alphabet, key=""):
        keyi = []
        if key:
            for char in key:
                index = al.get_index_in_alphabet(char, alphabet)
                keyi.append(index)
            # remove duplicates
            keyi = OrderedDict.fromkeys(keyi)

        alph_out = [alphabet[i] for i in keyi]

        for i in range(len(alphabet)):
            if i not in keyi:
                alph_out.append(alphabet[i])

        self.__alphabet = alph_out
        self.__side = int(math.ceil(math.sqrt(len(alphabet))))

    def get_coordinates(self, char):
        for j in range(len(self.__alphabet)):
            try:
                self.__alphabet[j].index(char)
                break
            except ValueError:
                pass

        return divmod(j, self.__side)

    def get_char(self, row, column):
        return self.__alphabet[row * self.__side + column][0]

    def get_columns(self):
        return self.__side

    def get_rows(self):
        return len(self.__alphabet) // self.__side
