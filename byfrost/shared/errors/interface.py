#!/usr/bin/env python3

from typing import Any


class BifrostError(Exception):
    def __init__(self, error: str = "", code: str = ""):
        super().__init__(error, code)
        self.Error = error
        self.Code = code

    def __str__(self):
        return self.Error

    def code(self):
        return self.Code

    def nil(self):
        return self.Error == "" and self.Code == ""
