#!/usr/bin/python

from .uppercase import UpperCase
from .lowercase import LowerCase
from .nospaces import NoSpaces
from .savespaces import SaveSpaces
from .savecase import SaveCase
from .save_all import SaveAll
from .remove_non_alphabet import RemoveNonAlphabet


__all__ = [
    "UpperCase", "LowerCase", "NoSpaces", "SaveSpaces", "SaveCase",
    "SaveAll", "RemoveNonAlphabet"
]
