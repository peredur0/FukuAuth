# coding: utf-8
"""
Initialize the database with the required collection.

If a collection already exists it can perform updates
"""

from utils import logging_utils, files_utils

logger = logging_utils.set_logger("init.main")

SCHEMA_FOLDER = "schemas"


def check_collection(file: str) -> None:
    """
    Check collection and schema based on schema file
    """
    pass


def main() -> None:
    """
    Main init process
    """
    logger.info("Getting collections schema files")
    schema_files = files_utils.list_files(SCHEMA_FOLDER, "_collection.json")
    logger.info("Collection files found - %i", len(schema_files))

    for file in schema_files:
        check_collection(file)


if __name__ == "__main__":
    main()
