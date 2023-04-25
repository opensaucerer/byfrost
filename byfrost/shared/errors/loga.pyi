#!/usr/bin/env python3

from typing import Any
import logging

def _get_logger(name: str) -> logging.Logger:
    """_get_logger returns a logger with the given name"""
    ...

def get_logger(name: str) -> logging.Logger:
    """get_logger calls _get_logger to return a logger with the given name"""
    ...

def warn(message: str, *args: Any, **kwargs: Any) -> None:
    """warn logs a warning message with color yellow"""
    ...

def error(message: str, *args: Any, **kwargs: Any) -> None:
    """error logs an error message with color red"""
    ...

def info(message: str, *args: Any, **kwargs: Any) -> None:
    """info logs an info message with color blue"""
    ...

def debug(message: str, *args: Any, **kwargs: Any) -> None:
    """debug logs a debug message with color green"""
    ...
