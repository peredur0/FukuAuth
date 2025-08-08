# coding: utf-8
"""
Library of function related to files management
"""

import os
from utils import logging_utils

logger = logging_utils.set_logger("files_utils")


def list_files(source: str, suffix: str = "", recursive: bool = True) -> list[str]:
    """
    Listing json file used to create collections in mongo
    """
    files = []
    for elem in os.listdir(source):
        filepath = os.path.join(source, elem)
        if os.path.isdir(filepath):
            if recursive:
                files += list_files(filepath, suffix, recursive)
            continue

        if suffix and not filepath.endswith(suffix):
            continue

        files.append(filepath)

    return files
