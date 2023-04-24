#!/usr/bin/env python3
"""
All type definitions relating to the bifrost bridge but using TypedDict

This is majorly for end users who want to pass a kwargs dict to the bifrost dataclass when using bifrost functions
"""
from typing import TypedDict
import sys

# You may also pick one without version check, of course but This is more backward compatible
if sys.version_info < (3, 11):
    from typing_extensions import NotRequired
else:
    from typing import NotRequired


class BridgeConfigDict(TypedDict):
    """
    BridgeConfigDict is the configuration for the rainbow bridge.

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
    zone: NotRequired[str]
    """zone is the service zone to use for storage."""
    default_bucket: NotRequired[str]
    """default_bucket is the default storage bucket to use for storing.
    This is only implemented by some providers (e.g. google cloud storage, s3)."""
    credentials_file: NotRequired[str]
    """credentials_file is the path to the credentials file.
    This is only implemented by some providers (e.g. google cloud storage)."""
    secret_key: NotRequired[str]
    """secret_key is the secret key for iam authentication.
    This is only implemented by some providers (e.g. s3)
    """
    access_key: NotRequired[str]
    """access_key is the access key for iam authentication.
        This is only implemented by some providers (e.g. s3)
    """
    region: NotRequired[str]
    """region is the service region to use for storing.
    This is only implemented by some providers (e.g. s3, google cloud storage)"""
    default_timeout: NotRequired[int]
    """default_timeout is the time-to-live for time-dependent storage operations."""
    enable_debug: NotRequired[bool]
    """enable_debug enables debug logging."""
    project: NotRequired[str]
    """project is the cloud project to use for storage.
        This is only implemented by some providers (e.g. google cloud storage)."""
    public_read: NotRequired[bool]
    """public_read enables public read access to uploaded files."""
    use_async: NotRequired[bool]
    """use_async enables asynchronous operations with any of asyncio, threads, queue, and multi-processing."""
    pinata_jwt: NotRequired[str]
    """pinata_jwt is the jwt generated for your pinata cloud account."""
