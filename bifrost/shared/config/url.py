#!/usr/bin/env python3

"""URL constants."""

URLPinataPinFile = "https://api.pinata.cloud/pinning/pinFileToIPFS"
"""URLPinataPinFile is the endpoint for pinning files/folders to Pinata cloud."""

URLPinataPinJSON = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
"""URLPinataPinJSON is the endpoint for pinning JSON objects to Pinata cloud."""

URLPinataPinCID = "https://api.pinata.cloud/pinning/pinByHash"
"""URLPinataPinCID is the endpoint for pinning CIDs to Pinata cloud."""

URLPinataAuth = "https://api.pinata.cloud/data/testAuthentication"
"""URLPinataAuth is the endpoint for testing authentication against provided Pinata credentials."""

URLPinataGateway = "https://gateway.pinata.cloud/ipfs/%v"
"""URLPinataGateway is the public gateway for Pinata cloud."""

URLGoogleCloudStorage = "https://storage.googleapis.com/%s/%s"
"""URLGoogleCloudStorage is the public gateway for Google Cloud Storage."""

URLSimpleStorageService = "https://%s.s3.%s.amazonaws.com/%s"
"""URLSimpleStorageService is the public gateway for Simple Storage Service."""
