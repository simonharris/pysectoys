"""
Linear Congruential Generator and Combined LCG
"""

from random import randint


class LCGParams():
    """ Value object describing the parameters for an instance of the LCG"""

    def __init__(self, modulus_m, multiplier_a, increment_c=0):
        self._modulus_m = modulus_m
        self._multiplier_a = multiplier_a
        self._increment_c = increment_c

    def get_modulus(self):
        return self._modulus_m

    def get_multiplier(self):
        return self._multiplier_a

    def get_increment(self):
        return self._increment_c


# Linear Congruential Generator -----------------------------------------------


class LCG():
    """Generates a linear congruential sequence via a Python generator"""

    def __init__(self, params):
        self._multiplier_a = params.get_multiplier()
        self._increment_c = params.get_increment()
        self._modulus_m = params.get_modulus()

    def generator(self, seed=None):
        """Increment is non-zero for mixed or 0 for multiplicative, as is
        required for combined generators"""

        # this just allows injecting an override for unit testing purposes
        if not seed:
            seed = randint(1, self._modulus_m-1)

        X = [seed]

        i = 0
        while True:
            X.append(self._multiplier_a * X[i] + self._increment_c)
            yield X[i] % self._modulus_m
            i += 1

    def get_modulus(self):
        return self._modulus_m

# Combined Linear Congruential Generator --------------------------------------


class CombinedLCG():
    """Combines n LCG objects to generate a Combined LC sequence"""

    def __init__(self, *lcgs):
        self._lcgs = lcgs

    def generator(self):

        m1 = self._lcgs[0]
        modulus = m1.get_modulus()

        j = 1
        while True:
            sum = 0
            for lcg in self._lcgs:
                sum += ((-1) ** (j-1)) * next(lcg.generator())

            yield sum % modulus
            j += 1
