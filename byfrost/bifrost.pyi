#!/usr/bin/env python3

"""
    The RainbowBridge interface for Google Cloud Storage

    All providers must implemented this interface completely
"""

from .shared.types.dataclass import bridge
from typing import Tuple
from .shared.errors.interface import BifrostError

def new_rainbow_bridge(
    bc: bridge.BridgeConfig,
) -> Tuple[bridge.RainbowBridge, BifrostError]:
    """
    new_rainbow_bridge returns a new Rainbow Bridge for shipping files to your specified cloud storage service and an error if one occurs.
    """
    ...
