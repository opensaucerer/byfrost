#!/usr/bin/env python3

"""Provider constants"""

PinataCloud = "pinata"
"""PinataCloud is the identifier of the Pinata Cloud storage."""

SimpleStorageService = "s3"
"""SimpleStorageService is the identifier of the S3 provider."""

GoogleCloudStorage = "gcs"
"""GoogleCloudStorage is the identifier of the Google Cloud Storage provider."""


providers = {
    "pinata": "Pinata Cloud Storage",
    "s3":     "Simple Storage Service",
    "gcs":    "Google Cloud Storage",
} 
"""providers is a map of the supported providers"""