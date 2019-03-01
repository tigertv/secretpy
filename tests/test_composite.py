#!/usr/bin/python
# -*- encoding: utf-8 -*-
import sys

from secretpy import CryptMachine
from secretpy import CompositeMachine
from unittest import TestCase, main

if sys.version_info[0] < 3:
    # Python 2
    from mock import patch, Mock
else:
    # Python 3
    from unittest.mock import patch, Mock


class TestCompositeMachine(TestCase):

    @patch('secretpy.Atbash')
    @patch('secretpy.Caesar')
    def test_main(self, Atbash, Caesar):
        cipher1 = Caesar()
        cipher1.encrypt.return_value = "CAESAR_ENCRYPTED"
        cipher1.decrypt.return_value = "CAESAR_DECRYPTED"

        cipher2 = Atbash()
        cipher2.encrypt.return_value = "ATBASH_ENCRYPTED"
        cipher2.decrypt.return_value = "ATBASH_DECRYPTED"

        cm1 = CryptMachine(Caesar(), 3)
        cm2 = CryptMachine(Atbash())
        cm = CompositeMachine(cm1, cm2)
        enc = cm.encrypt("text")
        dec = cm.decrypt(enc)

        self.assertEqual(enc, "ATBASH_ENCRYPTED")
        self.assertEqual(dec, "ATBASH_DECRYPTED")

        cipher2.encrypt.assert_called_with(
            "CAESAR_ENCRYPTED", "", u"abcdefghijklmnopqrstuvwxyz")
        cipher2.decrypt.assert_called_with(
            "CAESAR_DECRYPTED", "", u"abcdefghijklmnopqrstuvwxyz")


if __name__ == '__main__':
    main()
