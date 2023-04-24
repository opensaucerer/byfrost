#!/usr/bin/env python3

"""Bifrost interface for Google Cloud Storage"""

from ..shared.types.dataclass import file as bfile
from ..shared.types.dataclass import bridge
from typing import List, Tuple
from ..shared.errors.interface import BifrostError


class GoogleCloudStorage:
    def __init__(self, bc: bridge.BridgeConfig):
        pass

    def upload_file(file_face: bfile.File) -> Tuple[bfile.UploadedFile, BifrostError]:
        """
        bucket = storage_client.get_bucket(config.wm_bucket)
        blob = bucket.blob(p_file["title"])
        blob.upload_from_filename(
            f"{config.video_folder + '/' + utils.generate_wm_name(p_file['title'])}/{p_file['title']}"
        )
        blob.make_public()

        """
        pass

    def upload_multi_file(
        multi_face: bfile.MultiFile,
    ) -> Tuple[List[bfile.UploadedFile], BifrostError]:
        pass

    def disconnect() -> BifrostError:
        pass

    def config() -> bridge.BridgeConfig:
        pass

    def is_connected() -> bool:
        pass

    def upload_folder(
        fold_face: bfile.MultiFile,
    ) -> Tuple[List[bfile.UploadedFile], BifrostError]:
        pass
