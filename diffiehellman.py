"""
Diffie-Hellman key exchange algorithm
"""


class DiffieHellman():
    """Diffie-Hellman key exchange algorithm"""

    def __init__(self, q, alpha):
        self._prime_q = q
        self._alpha = alpha

    def calculate(self, private_a, private_b):

        public_a = (self._alpha ** private_a) % self._prime_q
        public_b = (self._alpha ** private_b) % self._prime_q

        secret_a = (public_b ** private_a) % self._prime_q
        secret_b = (public_a ** private_b) % self._prime_q

        return secret_a, secret_b
