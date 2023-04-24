#!/usr/bin/env python3

from byfrost import BifrostError
import unittest


class TestError(unittest.TestCase):
    def test_error(self):
        try:
            raise BifrostError("some stuff", "test")
        except BifrostError as e:
            self.assertEqual(e.code(), "test")


if __name__ == "__main__":
    unittest.main()
