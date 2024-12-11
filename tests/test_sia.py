# tests/test_module1.py

import unittest
from sia import Sia

class TestSia(unittest.TestCase):

    def test_add_string8(self):
        sia = Sia()
        sia.add_string8("Hello")
        sia.add_uint8(25)
        sia.add_string8("World")
        self.assertEqual(sia.content, bytearray(b'\x05Hello\x19\x05World'))

if __name__ == "__main__":
    unittest.main()