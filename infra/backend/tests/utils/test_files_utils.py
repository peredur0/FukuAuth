# coding: utf-8
"""
Tests for the file management module
"""

import pytest

from infra.backend.utils import files_utils


@pytest.fixture
def sample_rep(tmp_path):
    (tmp_path / "file1").write_text("no extension")
    (tmp_path / "file2.json").write_text("{}")
    (tmp_path / "file3_collection.json").write_text("{}")

    sub_dir = tmp_path / "subdir"
    sub_dir.mkdir()
    (sub_dir / "nested.json").write_text("{}")

    return tmp_path


class TestFileUtils:

    def test_list_files_json(self, sample_rep):
        result = files_utils.list_files(str(sample_rep), ".json")
        assert sorted(result) == sorted(
            [
                str(sample_rep / "file2.json"),
                str(sample_rep / "file3_collection.json"),
                str(sample_rep / "subdir" / "nested.json"),
            ]
        )

    def test_list_files_collection(self, sample_rep):
        result = files_utils.list_files(str(sample_rep), "_collection.json")
        assert result == [str(sample_rep / "file3_collection.json")]

    def test_list_files_not_recursive(self, sample_rep):
        result = files_utils.list_files(str(sample_rep), "", False)
        assert sorted(result) == sorted(
            [
                str(sample_rep / "file1"),
                str(sample_rep / "file2.json"),
                str(sample_rep / "file3_collection.json"),
            ]
        )
