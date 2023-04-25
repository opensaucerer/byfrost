#!/usr/bin/env python3

from .shared.types.dataclass.bridge import BridgeConfig, RainbowBridge
from .shared.errors.interface import BifrostError
from typing import Tuple, Union
from .shared.errors import constants as errors
from .shared.config import provider
from .shared.errors import loga
from google.cloud import storage


def new_rainbow_bridge(
    bc: BridgeConfig,
) -> Tuple[Union[RainbowBridge, None], BifrostError]:
    # verify that the config is valid
    if bc is None:
        return None, BifrostError("config is none", errors.ErrInvalidConfig)

    # verify that the config is derived from BridgeConfig
    if not isinstance(bc, BridgeConfig):
        return None, BifrostError(
            "invalid config type: {}".format(type(bc)), errors.ErrInvalidConfig
        )

    # verify that the config dataclass has a valid provider
    if bc.provider is None or bc.provider == "":
        return None, BifrostError("no provider specified", errors.ErrInvalidProvider)

    # verify that the provider is vaid
    if bc.provider not in provider.providers:
        return None, BifrostError(
            "invalid provider: {}".format(bc.provider), errors.ErrInvalidProvider
        )

    # verify that the config dataclass has a valid bucket
    if bc.default_bucket is None or bc.default_bucket == "":
        # some providers might not require a bucket
        # just log a warning
        if bc.enable_debug is True:
            loga.warn(
                "WARN: No bucket specified for provider: {}. This might cause errors or require you to specify a bucket for each operation.".format(
                    bc.provider
                )
            )

    # create a new bridge based on the provider
    if bc.provider == provider.GoogleCloudStorage:
        return new_google_cloud_storage(bc)

    return None, BifrostError(
        "invalid provider: {}".format(bc.provider), errors.ErrInvalidProvider
    )


def new_google_cloud_storage(
    bc: BridgeConfig,
) -> Tuple[Union[RainbowBridge, None], BifrostError]:
    client = storage.Client()
    return client, BifrostError()
