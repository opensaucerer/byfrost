#!/usr/bin/env python3
"""
All type definitions relating to the bifrost bridge but using dataclasses
"""
from dataclasses import dataclass
from typing import Optional, Callable, Any
from . import file as bfile
from typing import List, Tuple

from ...errors.interface import BifrostError


@dataclass
class BridgeConfig:
    """
    BridgeConfig is the configuration for the rainbow bridge.

    Attributes:

    provider {str} -- provider is the name of the cloud storage service to use.

    zone {str} -- zone is the service zone to use for storage.

    default_bucket {str} -- default_bucket is the default storage bucket to use for storing.
    This is only implemented by some providers (e.g. google cloud storage, s3).

    credentials_file {str} -- credentials_file is the path to the credentials file.

    secret_key {str} -- secret_key is the secret key for iam authentication.

    access_key {str} -- access_key is the access key for iam authentication.

    region {str} -- region is the service region to use for storing.
    This is only implemented by some providers (e.g. s3, google cloud storage).

    default_timeout {int} -- default_timeout is the time-to-live for time-dependent storage operations.

    enable_debug {bool} -- enable_debug enables debug logging.

    project {str} -- project is the cloud project to use for storage.
    This is only implemented by some providers (e.g. google cloud storage).

    public_read {bool} -- public_read enables public read access to uploaded files.

    use_async {bool} -- use_async enables asynchronous operations with any of asyncio, threads, queue, and multi-processing.

    pinata_jwt {str} -- pinata_jwt is the jwt generated for your pinata cloud account
    """

    provider: str
    """Provider is the name of the cloud storage service to use."""
    zone: Optional[str] = ""
    """zone is the service zone to use for storage."""
    default_bucket: Optional[str] = ""
    """default_bucket is the default storage bucket to use for storing.
    This is only implemented by some providers (e.g. google cloud storage, s3)."""
    credentials_file: Optional[str] = ""
    """credentials_file is the path to the credentials file.
    This is only implemented by some providers (e.g. google cloud storage)."""
    secret_key: Optional[str] = ""
    """secret_key is the secret key for iam authentication.
    This is only implemented by some providers (e.g. s3)
    """
    access_key: Optional[str] = ""
    """access_key is the access key for iam authentication.
        This is only implemented by some providers (e.g. s3)
    """
    region: Optional[str] = ""
    """region is the service region to use for storing.
    This is only implemented by some providers (e.g. s3, google cloud storage)"""
    default_timeout: Optional[int] = 0
    """default_timeout is the time-to-live for time-dependent storage operations."""
    enable_debug: Optional[bool] = False
    """enable_debug enables debug logging."""
    project: Optional[str] = ""
    """project is the cloud project to use for storage.
        This is only implemented by some providers (e.g. google cloud storage)."""
    public_read: Optional[bool] = False
    """public_read enables public read access to uploaded files."""
    use_async: Optional[bool] = False
    """use_async enables asynchronous operations with any of asyncio, threads, queue, and multi-processing."""
    pinata_jwt: Optional[str] = ""
    """pinata_jwt is the jwt generated for your pinata cloud account."""
    client: Optional[Any] = None


@dataclass
class RainbowBridge:
    """
    The RainbowBridge interface for Google Cloud Storage

    All providers must implement this interface completely
    """

    upload_file: Callable[[bfile.File], Tuple[bfile.UploadedFile, BifrostError]]
    """
    upload_file uploads a file to the provider storage and returns an error if one occurs.

    Note: for some providers, upload_file requires that a default bucket be set in bifrosbfile.BridgeConfig.
    """

    upload_multi_file: Callable[
        [bfile.MultiFile], Tuple[List[bfile.UploadedFile], BifrostError]
    ]
    """
    upload_multi_file uploads mutliple files to the provider storage and returns an error if one occurs. If any of the uploads fail, the error is appended to the []UploadedFile.Error and also logged when debug is enabled while the rest of the uploads continue.

    Note: for some providers, UploadMultiFile requires that a default bucket be set in bifrosbfile.BridgeConfig.
    """

    disconnect: Callable[[], BifrostError]
    """
    disconnect closes the provider client connection and returns an error if one occurs.

    Disconnect should only be called when the connection is no longer needed.
    """

    config: Callable[[], BridgeConfig]
    """
    config returns the provider configuration.
    """

    is_connected: Callable[[], bool]
    """
    is_connected returns true if there is an active connection to the provider.
    """

    upload_folder: Callable[
        [bfile.MultiFile], Tuple[List[bfile.UploadedFile], BifrostError]
    ]
    """
    upload_folder uploads a folder to the provider storage and returns an error if one occurs.

    Note: for some providers, upload_folder requires that a default bucket be set in bifrosbfile.BridgeConfig.
    """
