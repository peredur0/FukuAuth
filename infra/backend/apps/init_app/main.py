# coding: utf-8
"""
Initialize the database with the required collection.

If a collection already exists it can perform updates
"""

from utils import logging_utils

logger = logging_utils.set_logger("init.main")


def main() -> None:
    """
    Main init process
    """
    logger.info("INIT")
    print("foo")


if __name__ == "__main__":
    main()
