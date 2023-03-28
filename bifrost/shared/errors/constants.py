#!/usr/bin/env python3

"""Error constants."""

ErrBadRequest = "bad request"
"""ErrBadRequest is returned when something fails due to client error."""

ErrUnauthorized = "unauthorized"
"""ErrUnauthorized is returned when something fails due to client not being authorized."""

ErrInvalidConfig = "invalid config"
"""ErrInvalidConfig is returned when the config is invalid."""

ErrInvalidBucket = "invalid bucket"
"""ErrInvalidBucket is returned when the bucket is invalid."""

ErrInvalidProvider = "invalid provider"
"""ErrInvalidProvider is returned when the provider is invalid."""

ErrInvalidCredentials = "invalid credentials"
"""ErrInvalidCredentials is returned when the authentication credentials are invalid."""

ErrFileOperationFailed = "file operation failed"
"""ErrFileOperationFailed is returned when a file operation fails."""

ErrIncompleteMultiFileUpload = "incomplete files upload"
"""ErrIncompleteMultiFileUpload is returned when a multifile upload fails on some files."""

ErrClientError = "client error"
"""ErrClientError is returned when the client returns an error."""
