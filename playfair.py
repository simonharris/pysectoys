"""
Encode and decode text using a Playfair cipher

TODO: investigate the correct way to handle whitespace and casing. That wasn't
    part of the exercise
"""

# Constant name...doesn't conform to UPPER_CASE naming style
# pylint: disable=C0103

import math
import re


class PlayfairCipher:
    """Playfair Cipher algorithm"""

    ALPHABET = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # note: no J
    PADDING_CHAR = 'Z'  # this seems to be the convention, but not the law

    def __init__(self, key):
        self._create_key(key)

    # public methods ----------------------------------------------------------

    def encrypt(self, text):
        """Encrypts text using the Playfair cipher and the given key"""

        my_encrypted = ''

        for pair in self._split_into_pairs(self._clean_text(text)):
            my_encrypted = my_encrypted + self._encrypt_pair(pair)

        return my_encrypted

    def decrypt(self, text):
        """Decrypts text using the Playfair cipher and the given key"""

        decrypted = ''

        for pair in self._split_into_pairs(self._clean_text(text)):
            decrypted = decrypted + self._decrypt_pair(pair)

        return decrypted

    # private methods ---------------------------------------------------------

    def _create_key(self, string):
        """Creates the 25 character key table from an input string"""

        string = string.upper().replace('J', 'I')

        seen = []
        key = ''

        for char in string:
            if char not in seen:
                key = key + char
                seen.append(char)

        for char in self.ALPHABET:
            if char not in seen:
                key = key + char

        self._key_string = key

    @staticmethod
    def _clean_text(text):
        """Removes non-alphabet characters and normalises to upper case"""

        text = re.compile('[^a-zA-Z]').sub('', text)
        return text.upper()

    def _split_into_pairs(self, text):
        """
        Splits the plaintext into pairs of characters, adding
        padding if needed
        """

        if len(text) % 2 == 1:
            text = text + self.PADDING_CHAR

        pairs = []
        for i in range(0, len(text), 2):
            pair = [text[i], text[i + 1]]
            pairs.append(pair)

        return pairs

    def _encrypt_pair(self, pair):
        """Encrypt a character pair"""

        left = self._key_string.find(pair[0])
        right = self._key_string.find(pair[1])

        col_left = left % 5
        col_right = right % 5

        row_left = math.floor(left / 5)
        row_right = math.floor(right / 5)

        if col_left == col_right:
            new_left = (left + 5) % 25
            new_right = (right + 5) % 25

        elif row_left == row_right:
            row_max = row_left * 5 + 4
            new_left = (left + 1) if (left + 1) <= row_max else (left - 4)
            new_right = (right + 1) if (right + 1) <= row_max else (right - 4)

        else:
            col_shift = abs(col_left - col_right)

            if col_left < col_right:
                new_left = left + col_shift
                new_right = right - col_shift
            else:
                new_left = left - col_shift
                new_right = right + col_shift

        return self._key_string[new_left] + self._key_string[new_right]

    def _decrypt_pair(self, pair):

        left = self._key_string.find(pair[0])
        right = self._key_string.find(pair[1])

        col_left = left % 5
        col_right = right % 5

        row_left = math.floor(left / 5)
        row_right = math.floor(right / 5)

        if col_left == col_right:
            new_left = (left - 5) if (left - 5 > 0) else (left + 20)
            new_right = (right - 5)

        elif row_left == row_right:
            row_min = row_left * 5
            new_left = (left - 1) if (left - 1) >= row_min else (left + 4)
            new_right = (right - 1) if (right - 1) >= row_min else (right + 4)

        else:
            col_shift = abs(col_left - col_right)

            if col_left < col_right:
                new_left = left + col_shift
                new_right = right - col_shift
            else:
                new_left = left - col_shift
                new_right = right + col_shift

        return self._key_string[new_left] + self._key_string[new_right]

    # test helper methods -----------------------------------------------------

    def get_key(self):
        """Accessor for the encryption key"""

        return self._key_string


# the interactive part of the program -----------------------------------------

if __name__ == '__main__':

    mode = input('Would you like to encrypt or decrypt? (e/d) ')

    if mode == 'e':
        plaintext = input('Please input plaintext: ')
        keycode = input('Please input key: ')

        pf = PlayfairCipher(keycode)

        encrypted = pf.encrypt(plaintext)
        print('Your encrypted text is as follows: ')
        print('')
        print(encrypted)

    elif mode == 'd':

        ciphertext = input('Please input ciphertext: ')
        keycode = input('Please input key: ')

        pf = PlayfairCipher(keycode)

        encrypted = pf.decrypt(ciphertext)
        print('Your decrypted text is as follows: ')
        print('')
        print(encrypted)

    else:
        print('Did not recognise option')
