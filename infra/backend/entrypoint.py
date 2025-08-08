# coding: utf-8
"""
Entrypoint to know which process to start
- init: start the full init process
- api: run the API server
"""

import sys
import subprocess

from utils import logging_utils

logger = logging_utils.set_logger(__name__)

try:
    process = sys.argv[1]
except IndexError:
    logger.error("Missing arguments to run any process")
    sys.exit(1)


match process:
    case "init":
        logger.info("Start init process")
        result = subprocess.run(
            ["python3", "apps/init_app/main.py"], env={"PYTHONPATH": "."}
        )
    case _:
        logger.error("Unknown command - %s", process)
        sys.exit(1)

sys.exit(result.returncode)
