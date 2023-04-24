#!/usr/bin/env python3


class BifrostError(Exception):
    def __init__(self, error, code, *args):
        super().__init__(args)
        self.Error = error
        self.Code = code

    def __str__(self):
        return self.Error

    def code(self):
        return self.Code

    def nil(self):
        return self.Error == "" and self.Code == ""
