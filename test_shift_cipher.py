import unittest
from ciphers.shift_cipher import ShiftCipher
from ciphers.exceptions.unknowntype_error import UnknownTypeError

class TestShiftCipher(unittest.TestCase):
    def setUp(self):
        self.shift_cipher = ShiftCipher("Hello World")

    def test_constructor(self):
        with self.assertRaises(UnknownTypeError):
            ShiftCipher(3)

    def test_encrypt(self):
        self.assertEqual(self.shift_cipher.encrypt(), "Khoor Zruog")
        self.shift_cipher.given_string = "KOKO"
        self.assertEqual(self.shift_cipher.encrypt(), "NRNR")

    def test_decrypt(self):
        self.shift_cipher.given_string = "Khoor Zruog"
        self.assertEqual(self.shift_cipher.decrypt(), "Hello World")
        self.shift_cipher.given_string = "NRNR"
        self.assertEqual(self.shift_cipher.decrypt(), "KOKO")

if __name__ == '__main__':
    unittest.main()
