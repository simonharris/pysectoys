"""
Tests for the Playfair cipher
"""

import unittest

from playfair import PlayfairCipher


class TestPlayfair(unittest.TestCase):
    """Playfair Cipher algorithm"""

    KEY = 'githubcom'
    PLAINTEXT = 'ENIGMATICVARIATIONS'
    CIPHERTEXT = 'DPTIABHTBWMSUCHTBQZU'

    def setUp(self):

        self.cipher = PlayfairCipher(self.KEY)


    def test_encrypt(self):

        encrypted = self.cipher.encrypt(self.PLAINTEXT)
        self.assertEqual(encrypted, self.CIPHERTEXT)


    def test_decrypt(self):

        decrypted = self.cipher.decrypt(self.CIPHERTEXT)
        self.assertEqual(decrypted, self.PLAINTEXT + PlayfairCipher.PADDING_CHAR)


    def test_both_ways(self):
        """Extra test just to be 100% certain"""

        other_text = 'SOMEOTHERTEXT'

        encrypted = self.cipher.encrypt(other_text)
        self.assertEqual(self.cipher.decrypt(encrypted), other_text + PlayfairCipher.PADDING_CHAR)
