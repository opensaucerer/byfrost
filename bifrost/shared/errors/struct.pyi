#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Any

class BifrostError(Exception):
    """BifrostError is the class for all bifrost exceptions"""

    # Error is the error message
    Error: str
    # Code is the error code
    Code: str

    def __init__(self, error: str, code: str, *args: Any): ...
    # __str__ returns the error message
    def __str__(self) -> str: ...
    # code returns the error code
    def code(self) -> str: ...
