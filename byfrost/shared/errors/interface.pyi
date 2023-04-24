#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Any

class BifrostError(Exception):
    """BifrostError is the class for all bifrost BifrostErrors"""

    Error: str
    """Error is the error message"""
    Code: str
    """Code is the error code"""

    def __init__(self, error: str, code: str, *args: Any): ...
    def __str__(self) -> str:
        """__str__ returns the error message"""
        ...
    def code(self) -> str:
        """code returns the error code"""
        ...
    def nil(self) -> bool:
        """nil returns true if the error is nil"""
        ...
