#!/usr/bin/env python3

"""
bifrost provides a rainbow bridge for shipping files to any cloud storage service.

It's like bifrost from marvel comics, but for files.
"""

from .shared.types.dataclass.bridge import BridgeConfig, RainbowBridge
from .shared.errors.constants import (
    ErrBadRequest,
    ErrClientError,
    ErrIncompleteMultiFileUpload,
    ErrInvalidBucket,
    ErrInvalidConfig,
    ErrInvalidCredentials,
    ErrInvalidProvider,
    ErrUnauthorized,
    ErrFileOperationFailed,
)
from .shared.errors.interface import BifrostError
from .shared.config.provider import (
    GoogleCloudStorage,
    PinataCloud,
    SimpleStorageService,
)
from .shared.types.dataclass.file import (
    File,
    MultiFile,
)
from .bifrost import new_rainbow_bridge

__name__ = "byfrost"
