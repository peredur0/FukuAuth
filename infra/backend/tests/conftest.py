# coding: utf-8
"""
Start the test environment
"""

import pytest
import subprocess

from infra.backend.utils import mongo_utils


@pytest.fixture(scope="session", autouse=True)
def manage_test_environment():
    subprocess.run(["./scripts/manage_env.sh", "test", "start"], check=True)

    mongo_utils.wait_for_mongo("mongodb://localhost:27018")
    yield

    subprocess.run(["./scripts/manage_env.sh", "test", "stop"], check=True)
