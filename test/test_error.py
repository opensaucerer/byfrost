#!/usr/bin/env python3

import byfrost
import unittest


class TestError(unittest.TestCase):
    def test_error(self):
        try:
            raise byfrost.BifrostError("some stuff", "test")
        except byfrost.BifrostError as e:
            self.assertEqual(e.code(), "test")


if __name__ == "__main__":
    unittest.main()
