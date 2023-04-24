#!/usr/bin/env python3

"""Bifrost interface for Google Cloud Storage"""

from ..shared.types.dataclass import file as bfile
from ..shared.types.dataclass import bridge
from typing import List, Tuple
from ..shared.errors.interface import BifrostError


class GoogleCloudStorage:
    """GoogleCloudStorage is the Google Cloud Storage class"""

    def upload_file(file_face: bfile.File) -> Tuple[bfile.UploadedFile, BifrostError]:
        """
        upload_file uploads a file to the provider storage and returns an error if one occurs.

        Note: for some providers, upload_file requires that a default bucket be set in bifrosbfile.BridgeConfig.
        """
        ...

    def upload_multi_file(
        multi_face: bfile.MultiFile,
    ) -> Tuple[List[bfile.UploadedFile], BifrostError]:
        """
        upload_multi_file uploads mutliple files to the provider storage and returns an error if one occurs. If any of the uploads fail, the error is appended to the []UploadedFile.Error and also logged when debug is enabled while the rest of the uploads continue.

        Note: for some providers, UploadMultiFile requires that a default bucket be set in bifrosbfile.BridgeConfig.
        """
        ...

    def disconnect() -> BifrostError:
        """
        disconnect closes the provider client connection and returns an error if one occurs.

        Disconnect should only be called when the connection is no longer needed.
        """
        ...

    def config() -> bridge.BridgeConfig:
        """
        config returns the provider configuration.
        """
        ...

    def is_connected() -> bool:
        """
        is_connected returns true if there is an active connection to the provider.
        """
        ...

    def upload_folder(
        fold_face: bfile.MultiFile,
    ) -> Tuple[List[bfile.UploadedFile], BifrostError]:
        """
        upload_folder uploads a folder to the provider storage and returns an error if one occurs.

        Note: for some providers, upload_folder requires that a default bucket be set in bifrosbfile.BridgeConfig.
        """
        ...
