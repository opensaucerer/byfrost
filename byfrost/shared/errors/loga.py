#!/usr/bin/env python3

import logging
from typing import Any


def _get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger


def get_logger(name: str) -> logging.Logger:
    return _get_logger(name)


def warn(message: str, *args: Any, **kwargs: Any) -> None:
    logger = _get_logger("byfrost")
    logger.warning(message, *args, **kwargs)
    return


def error(message: str, *args: Any, **kwargs: Any) -> None:
    logger = _get_logger("byfrost")
    logger.error(message, *args, **kwargs)


def info(message: str, *args: Any, **kwargs: Any) -> None:
    logger = _get_logger("byfrost")
    logger.info(message, *args, **kwargs)
    return


def debug(message: str, *args: Any, **kwargs: Any) -> None:
    logger = _get_logger("byfrost")
    logger.debug(message, *args, **kwargs)
    return
