#!/usr/bin/env python3


class BifrostError(Exception):
    """BifrostError is the class for all bifrost exceptions"""

    def __init__(self, error, code, *args):
        super().__init__(args)
        self.Error = error
        """Error is the error message"""
        self.Code = code
        """Code is the error code"""

    def __str__(self):
        """__str__ returns the error message"""
        return self.Error

    def code(self):
        """code returns the error code"""
        return self.Code
