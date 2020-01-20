"""
Tests for the Rivest Cipher 4 algorithm
"""

# Missing method docstring
# pylint: disable=C0111

import unittest

from rc4 import RC4


class TestRC4(unittest.TestCase):
    """Tests for the Rivest Cipher 4 algorithm"""

    def test_encrypt(self):
        rc4 = RC4('Key')
        self.assertEqual(rc4.encrypt('plaintext'),
                         '9B F3 16 E8 D9 40 AF 0A D3')

    def test_decrypt(self):
        rc4 = RC4('Key')
        self.assertEqual(rc4.decrypt('9B F3 16 E8 D9 40 AF 0A D3'),
                         'plaintext')

    def test_both(self):
        rc4 = RC4('Key')
        self.assertEqual(rc4.encrypt('plaintext'),
                         '9B F3 16 E8 D9 40 AF 0A D3')
        self.assertEqual(rc4.decrypt('9B F3 16 E8 D9 40 AF 0A D3'),
                         'plaintext')
