# coding: utf-8
"""
Tests for logging utils
"""
import logging
from infra.backend.utils import logging_utils


class TestLoggingUtils:

    def test_set_logger_info(self):
        test_logger_info = logging_utils.set_logger("logger1")
        assert test_logger_info.name == "logger1"
        assert test_logger_info.level == logging.INFO

    def test_set_logger_debug(self):
        test_logger_debug = logging_utils.set_logger("logger2", "debug")
        assert test_logger_debug.level == logging.DEBUG
