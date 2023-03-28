#!/usr/bin/env python3
"""
All type definitions relating to the bifrost bridge but using dataclasses
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class BridgeConfig:
    """
    BridgeConfig is the configuration for the rainbow bridge.

    Attributes:

    provider {str} -- provider is the name of the cloud storage service to use.

    zone {str} -- zone is the service zone to use for storage.

    default_bucket {str} -- default_bucket is the default storage bucket to use for storing.
    this is only implemented by some providers (e.g. google cloud storage, s3).

    credentials_file {str} -- credentials_file is the path to the credentials file.

    secret_key {str} -- secret_key is the secret key for iam authentication.

    access_key {str} -- access_key is the access key for iam authentication.

    region {str} -- region is the service region to use for storing.
    this is only implemented by some providers (e.g. s3, google cloud storage).

    default_timeout {int} -- default_timeout is the time-to-live for time-dependent storage operations.

    enable_debug {bool} -- enable_debug enables debug logging.

    project {str} -- project is the cloud project to use for storage.
    this is only implemented by some providers (e.g. google cloud storage).

    public_read {bool} -- public_read enables public read access to uploaded files.

    use_async {bool} -- use_async enables asynchronous operations with any of asyncio, threads, queue, and multi-processing.

    pinata_jwt {str} -- pinata_jwt is the jwt generated for your pinata cloud account
    """

    # Provider is the name of the cloud storage service to use.
    provider: str
    # zone is the service zone to use for storage.
    zone: Optional[str] = ""
    # default_bucket is the default storage bucket to use for storing.
    # this is only implemented by some providers (e.g. google cloud storage, s3).
    default_bucket: Optional[str] = ""
    # credentials_file is the path to the credentials file.
    # this is only implemented by some providers (e.g. google cloud storage).
    credentials_file: Optional[str] = ""
    # secret_key is the secret key for iam authentication.
    secret_key: Optional[str] = ""
    # access_key is the access key for iam authentication.
    access_key: Optional[str] = ""
    # region is the service region to use for storing.
    # this is only implemented by some providers (e.g. s3, google cloud storage).
    # endregion (this is just to prevent mypy from raising a type check error)
    region: Optional[str] = ""
    # default_timeout is the time-to-live for time-dependent storage operations.
    default_timeout: Optional[int] = 0
    # enable_debug enables debug logging.
    enable_debug: Optional[bool] = False
    # project is the cloud project to use for storage.
    # this is only implemented by some providers (e.g. google cloud storage).
    project: Optional[str] = ""
    # public_read enables public read access to uploaded files.
    public_read: Optional[bool] = False
    # use_async enables asynchronous operations with any of asyncio, threads, queue, and multi-processing.
    use_async: Optional[bool] = False
    # pinata_jwt is the jwt generated for your pinata cloud account
    pinata_jwt: Optional[str] = ""
