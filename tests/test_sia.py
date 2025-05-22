# tests/test_sia.py

import unittest
from sia import Sia

class TestSia(unittest.TestCase):

    def test_add_and_read_uint8(self):
        sia = Sia().add_uint8(255)
        self.assertEqual(sia.content, b'\xff')
        sia.seek(0)
        self.assertEqual(sia.read_uint8(), 255)

    def test_add_and_read_int8(self):
        sia = Sia().add_int8(-128).add_int8(127)
        self.assertEqual(sia.content, b'\x80\x7f')
        sia.seek(0)
        self.assertEqual(sia.read_int8(), -128)
        self.assertEqual(sia.read_int8(), 127)

    def test_add_and_read_uint16(self):
        sia = Sia().add_uint16(65535)
        self.assertEqual(sia.content, b'\xff\xff')
        sia.seek(0)
        self.assertEqual(sia.read_uint16(), 65535)

    def test_add_and_read_int16(self):
        sia = Sia().add_int16(-32768).add_int16(32767)
        self.assertEqual(sia.content, b'\x00\x80\xff\x7f')
        sia.seek(0)
        self.assertEqual(sia.read_int16(), -32768)
        self.assertEqual(sia.read_int16(), 32767)

    def test_add_and_read_uint32(self):
        sia = Sia().add_uint32(4294967295)
        self.assertEqual(sia.content, b'\xff\xff\xff\xff')
        sia.seek(0)
        self.assertEqual(sia.read_uint32(), 4294967295)

    def test_add_and_read_int32(self):
        sia = Sia().add_int32(-2147483648).add_int32(2147483647)
        sia.seek(0)
        self.assertEqual(sia.read_int32(), -2147483648)
        self.assertEqual(sia.read_int32(), 2147483647)

    def test_add_and_read_uint64(self):
        sia = Sia().add_uint64(2**64 - 1)
        sia.seek(0)
        self.assertEqual(sia.read_uint64(), 2**64 - 1)

    def test_add_and_read_int64(self):
        sia = Sia().add_int64(-2**63).add_int64(2**63 - 1)
        sia.seek(0)
        self.assertEqual(sia.read_int64(), -2**63)
        self.assertEqual(sia.read_int64(), 2**63 - 1)

    def test_add_and_read_bool(self):
        sia = Sia().add_bool(True).add_bool(False)
        self.assertEqual(sia.content, b'\x01\x00')
        sia.seek(0)
        self.assertTrue(sia.read_bool())
        self.assertFalse(sia.read_bool())

    def test_add_and_read_big_int(self):
        big = 2**128 + 123456789
        sia = Sia().add_big_int(big)
        sia.seek(0)
        self.assertEqual(sia.read_big_int(), big)

    def test_add_and_read_array8(self):
        arr = [1, 2, 3]
        sia = Sia().add_array8(arr, lambda s, x: s.add_uint8(x))
        sia.seek(0)
        result = sia.read_array8(lambda s: s.read_uint8())
        self.assertEqual(result, arr)

    def test_add_and_read_array16(self):
        arr = [1000, 2000]
        sia = Sia().add_array16(arr, lambda s, x: s.add_uint16(x))
        sia.seek(0)
        result = sia.read_array16(lambda s: s.read_uint16())
        self.assertEqual(result, arr)

    def test_add_and_read_array32(self):
        arr = [1 << 30, 2 << 30]
        sia = Sia().add_array32(arr, lambda s, x: s.add_uint32(x))
        sia.seek(0)
        result = sia.read_array32(lambda s: s.read_uint32())
        self.assertEqual(result, arr)

    def test_add_and_read_array64(self):
        arr = [1 << 60, 2 << 60]
        sia = Sia().add_array64(arr, lambda s, x: s.add_uint64(x))
        sia.seek(0)
        result = sia.read_array64(lambda s: s.read_uint64())
        self.assertEqual(result, arr)

    def test_embed_sia(self):
        s1 = Sia().add_uint8(42)
        s2 = Sia().add_uint8(99).embed_sia(s1)
        self.assertEqual(s2.content, b'\x63\x2a')

    def test_embed_bytes(self):
        s = Sia().add_uint8(1).embed_bytes(b'\x02\x03')
        self.assertEqual(s.content, b'\x01\x02\x03')

    def test_add_and_read_byte_array16(self):
        data = b"hello world"
        sia = Sia().add_byte_array16(data)
        sia.seek(0)
        self.assertEqual(sia.read_byte_array16(), data)

    def test_add_and_read_byte_array32(self):
        data = b"abcdefg"
        sia = Sia().add_byte_array32(data)
        sia.seek(0)
        result = sia.read_byte_array32()
        self.assertEqual(result, data)

    def test_add_and_read_byte_array64(self):
        data = b"large data" * 1000
        sia = Sia().add_byte_array64(data)
        sia.seek(0)
        self.assertEqual(sia.read_byte_array64(), data)

    def test_add_and_read_string16(self):
        s = "سلام"
        sia = Sia().add_string16(s)
        sia.seek(0)
        self.assertEqual(sia.read_string16(), s)

    def test_add_and_read_string32(self):
        s = "👋" * 100
        sia = Sia().add_string32(s)
        sia.seek(0)
        self.assertEqual(sia.read_string32(), s)

    def test_add_and_read_string8(self):
        sia = Sia().add_string8("Hello")
        self.assertEqual(sia.content, b'\x05Hello')
        sia.seek(0)
        self.assertEqual(sia.read_string8(), "Hello")

    def test_add_and_read_string64(self):
        text = "long string here!"
        sia = Sia().add_string64(text)
        sia.seek(0)
        self.assertEqual(sia.read_string64(), text)

    def test_write_and_read_string_n(self):
        s = Sia().write_string_n("abc")
        s.seek(0)
        self.assertEqual(s.read_string_n(3), "abc")

if __name__ == "__main__":
    unittest.main()
