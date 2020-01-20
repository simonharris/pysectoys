"""
Rivest Cipher 4 algorithm
"""


class RC4():
    """Rivest Cipher 4 algorithm"""

    def __init__(self, key):
        self._key = key
        self._S = []
        self._T = []
        self._build_arrays()

    def _build_arrays(self):

        keylength = len(self._key)

        for i in range(0, 256):
            self._S.append(i)
            charindex = i % keylength
            self._T.append(ord(self._key[charindex]))

        j = 0
        for i in range(0, 256):
            j = (j + self._S[i] + self._T[i]) % 256
            self._S[i], self._S[j] = self._S[j], self._S[i]

    def encrypt(self, plaintext):

        hextext = []

        S = self._S.copy()

        # TODO: I would love not to have duplicated this logic
        i = 0
        j = 0
        for char in plaintext:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]

            t = (S[i] + S[j]) % 256
            k = S[t]

            hextext.append("%02X" % (ord(char) ^ k))

        return ' '.join(hextext)

    def decrypt(self, ciphertext):

        output = ''

        hextext = ciphertext.split(' ')
        dec = [int(chunk, 16) for chunk in hextext]

        S = self._S.copy()

        i = 0
        j = 0
        for num in dec:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]

            t = (S[i] + S[j]) % 256
            k = S[t]

            output = output + chr(num ^ k)

        return output
