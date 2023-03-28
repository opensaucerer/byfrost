#!/usr/bin/env python3


class BifrostError(Exception):
    """BifrostError is the class for all bifrost exceptions"""

    def __init__(self, error, code, *args):
        super().__init__(args)
        self.Error = error
        self.Code = code

    # __str__ returns the error message
    def __str__(self):
        return self.Error

    # code returns the error code
    def code(self):
        return self.Code
