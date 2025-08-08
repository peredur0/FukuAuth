# coding: utf-8
"""
Library to interact with mongo db
"""
import time
import pymongo
from utils import logging_utils

logger = logging_utils.set_logger("mongo_utils")


def wait_for_mongo(uri: str, timeout=10) -> None:
    """
    Wait until mongo is ready for connections
    """
    client = pymongo.MongoClient(uri)
    start = time.time()

    while True:
        try:
            client.admin.command("ping")
            break
        except Exception:
            if time.time() - start > timeout:
                raise TimeoutError("MongoDB did not start in time")
        time.sleep(0.5)
