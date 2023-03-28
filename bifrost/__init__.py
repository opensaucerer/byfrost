"""
bifrost provides a rainbow bridge for shipping files to any cloud storage service.

It's like bifrost from marvel comics, but for files.
"""

from .shared.errors.color import (
    ERROR,
    INFO,
    NONE,
    OK,
    RESET,
    WARN,
)
from .shared.types.dataclass.bridge import BridgeConfig
from shared.errors.constants import (
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
from .shared.errors.struct import BifrostError
