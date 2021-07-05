#!/usr/bin/python
# -*- encoding: utf-8 -*-
import sys

from secretpy.cryptmachine import CryptMachine
from unittest import TestCase, main

if sys.version_info[0] < 3:
    # Python 2
    from mock import patch
else:
    # Python 3
    from unittest.mock import patch


class TestCryptMachine(TestCase):

    @patch('secretpy.Caesar')
    def test_main(self, Caesar):
        cipher = Caesar()
        cipher.encrypt.return_value = "ENCRYPTED"
        cipher.decrypt.return_value = "DECRYPTED"

        cm = CryptMachine(cipher, 5)
        enc = cm.encrypt("text")
        dec = cm.decrypt(enc)

        self.assertEqual(enc, "ENCRYPTED")
        self.assertEqual(dec, "DECRYPTED")

        cipher.encrypt.assert_called_with(
            "text", 5, u"abcdefghijklmnopqrstuvwxyz")
        cipher.decrypt.assert_called_with(
            "encrypted", 5, u"abcdefghijklmnopqrstuvwxyz")


if __name__ == '__main__':
    main()
