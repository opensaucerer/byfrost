#!/usr/bin/env python3
"""
All type definitions relating to files in bifrost but using TypedDict

This is majorly for end users who want to pass a kwargs dict to the bifrost dataclass when using bifrost functions
"""
from typing import TypedDict, Any, List, Dict
import sys
from ...errors.interface import BifrostError

# You may also pick one without version check, of course but this is more backward compatible
if sys.version_info < (3, 11):
    from typing_extensions import NotRequired
else:
    from typing import NotRequired
import queue


class OptionsDict(TypedDict):
    """Options is a dict of options to store along with each file

    Attributes:
        metadata {Dict[str, Any]} -- metadata is a map of metadata to store along with each file

        acl {str} -- acl is the access control list to specify the visibility of the file
        public: anyone can access the file
        private: only authenticated users can access the file

        content_type {str} -- content_type is the content type of the file
    """

    metadata: NotRequired[Dict[str, Any]]
    """metadata is a map of metadata to store along with each file."""
    acl: NotRequired[str]
    """acl is the access control list to specify the visibility of the file
        public: anyone can access the file
        private: only authenticated users can access the file."""
    content_type: NotRequired[str]
    """content_type is the content type of the file."""


class FileDict(TypedDict):
    """File is the dict for uploading a single file

    Attributes:
        path {str} -- path is the path to the file.

        filename {str} -- filename is the name to store the file as with the provider.

        options {Options} -- options is a dict of options to store along with each file.
    """

    path: str
    """path is the path to the file."""
    filename: NotRequired[str]
    """filename is the name to store the file as with the provider."""
    options: NotRequired[OptionsDict]
    """options is a dict of options to store along with each file."""


class MultiFileDict(TypedDict):
    """MultiFile is the dict for uploading multiple files.
    Along with options, you can also set global options that will be applied to all files.

    Attributes:
        files {List[File]} -- files is a list of files to upload

        global_options {Options} -- global_options is a map of options to store along with all the files.
        say 3 of 4 files need to share the same option, you can set globally for those 3 files and set the 4th file's option separately, bifrost won't override the option.
    """

    files: List[FileDict]
    """files is a list of files to upload."""
    global_options: NotRequired[OptionsDict]
    """
    GlobalOptions is a map of options to store along with all the files.
        
    Say 3 of 4 files need to share the same option, you can set globally for those 3 files and set the 4th file's option separately, bifrost won't override the option."""


class ParamFileDict(TypedDict):
    """ParamFile is the dict for uploading a single file in a multipart request.

    Attributes:
        name {str} -- name is the name of the file.

        path {str} -- path is the path to the file.

        key {str} -- key is the key to use for the file.
    """

    name: str
    """name is the name of the file."""
    path: str
    """path is the path to the file."""
    key: str
    """key is the key to use for the file."""


class ParamDataDict(TypedDict):
    """ParamData is the dict for uploading data along with files in a multipart request.

    Attributes:
        key {str} -- key is the key to use for the data.

        value {str} -- value is the value to use for the data.
    """

    key: str
    """key is the key to use for the data."""
    value: str
    """value is the value to use for the data."""


class ParamDict(TypedDict):
    """Param is the dict used to pass parameters to request methods

    Attributes:
        files {List[ParamFile]} -- files is a list of files to upload.

        data {List[ParamData]} -- data is a list of data to upload along with the files.
    """

    files: List[ParamFileDict]
    """files is a list of files to upload."""
    data: List[ParamDataDict]
    """data is a list of data to upload along with the files."""


class UploadedFileDict(TypedDict):
    """UploadedFile is the dict representing a completed file/files upload.

    Attributes:
        name {str} -- name is the name of the file.

        bucket {str} -- bucket is the bucket the file was uploaded to.

        path {str} -- path is the local path to the file.

        size {int} -- size is the size of the file in bytes.

        url {str} -- url is the location of the file in the cloud.

        preview {str} -- preview is the url to a preview of the file.

        provider_object {Any} -- provider_object is the object returned by the cloud storage provider.
        you need to cast it to the appropriate type before using it.

        done {queue.Queue} -- done sends a message to signal when an async process is complete.

        quit {queue.Queue} -- quit receives a message to signal for an exit of an async process.

        cid {str} -- cid is the content identifier for the file.
        this is only implemented by some providers (e.g. Pinata Cloud)

        error {BifrostError} -- error is the error returned by the provider. This is only used for async operations and multi file uploads.
    """

    name: str
    """name is the name of the file."""
    path: str
    """path is the local path to the file."""
    size: int
    """size is the size of the file in bytes."""
    url: str
    """url is the location of the file in the cloud."""
    preview: str
    """preview is the url to a preview of the file."""
    provider_object: Any
    """provider_object is the object returned by the cloud storage provider.
        you need to cast it to the appropriate type before using it."""
    bucket: NotRequired[str]
    """bucket is the bucket the file was uploaded to."""
    done: NotRequired[queue.Queue]
    """done sends a message to signal when an async process is complete."""
    quit: NotRequired[queue.Queue]
    """quit receives a message to signal for an exit of an async process."""
    cid: NotRequired[str]
    """cid is the content identifier for the file.
        this is only implemented by some providers (e.g. Pinata Cloud)"""
    error: NotRequired[BifrostError]
    """error is the error returned by the provider. This is only used for async operations and multi file uploads."""
