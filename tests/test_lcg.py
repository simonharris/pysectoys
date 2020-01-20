"""
Tests for the Linear Congruential Generator and Combined LCG
"""

import unittest

from lcg import LCGParams, LCG, CombinedLCG  # , DiffieHellman, RC4


class TestLGCParams(unittest.TestCase):

    def test_construction(self):
        config = LCGParams(12, 14)
        self.assertEqual(config.get_modulus(), 12)
        self.assertEqual(config.get_multiplier(), 14)

    def test_increment(self):
        config = LCGParams(12, 14)
        self.assertEqual(config.get_increment(), 0)

        config = LCGParams(12, 14, 123)
        self.assertEqual(config.get_increment(), 123)


class TestLCG(unittest.TestCase):

    # example from the lecture
    def test_slides_example(self):

        lcg = LCG(LCGParams(10, 7, 7))
        generator = lcg.generator(7)

        iterations = 6
        sequence = []

        i = 0
        while i < iterations:
            sequence.append(next(generator))
            i += 1

        self.assertEqual(sequence[0], 7)
        self.assertEqual(sequence[1], 6)
        self.assertEqual(sequence[2], 9)
        self.assertEqual(sequence[3], 0)
        self.assertEqual(sequence[4], 7)
        self.assertEqual(sequence[5], 6)

    # example from the assignment
    def test_assignment_example(self):
        modulus = 2147483642
        multiplier = 450

        lcg = LCG(LCGParams(modulus, multiplier))
        generator = lcg.generator()

        for i in range(0, 100):
            entry = next(generator)
            self.assertTrue(0 <= entry < modulus)

    # because the CLCG needs to know the modulus from the first LCG
    def test_get_modulus(self):
        lcg = LCG(LCGParams(10, 7, 7))
        self.assertEqual(lcg.get_modulus(), 10)


class TestCombinedLCG(unittest.TestCase):

    # it's hard to assert a random number is 'correct' so let's test that a
    # whole bunch of them at least look sane
    def test_as_best_as_i_can(self):

        m1 = 2147483642
        a1 = 450

        m2 = 2147483423
        a2 = 234

        lcg1 = LCG(LCGParams(m1, a1))
        lcg2 = LCG(LCGParams(m2, a2))

        generator = CombinedLCG(lcg1, lcg2).generator()

        for i in range(0, 100):
            mynext = next(generator)
            self.assertTrue(0 < mynext <= m1)
