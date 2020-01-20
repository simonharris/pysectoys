"""
Tests for Diffie-Hellman key exchange algorithm
"""

import unittest

from diffiehellman import DiffieHellman


class TestDiffieHellman(unittest.TestCase):

    def test_slides_example(self):
        """The example from the lecture slides"""

        prime = 353
        alpha = 3

        dh = DiffieHellman(prime, alpha)
        secreta, secretb = dh.calculate(97, 233)

        self.assertEqual(secreta, 160)
        self.assertEqual(secretb, 160)
