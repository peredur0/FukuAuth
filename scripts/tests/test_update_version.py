# coding: utf-8
"""
Tests for the automatic version update script
"""
import pytest
from scripts import update_version


class TestUpdateVersion:

    @pytest.mark.parametrize(
        "mode, version, expected",
        [
            ("patch", "1.2.3", "1.2.4"),
            ("minor", "1.2.3", "1.3.0"),
            ("major", "1.2.3", "2.0.0"),
        ],
    )
    def test_update(self, mode, version, expected):
        assert update_version.update(version, mode) == expected

    @pytest.mark.parametrize(
        "msg, expected",
        [
            ("fix: typo", "patch"),
            ("fix(api): typo", "patch"),
            ("feat: new endpoint", "minor"),
            ("feat!: removed endpoint", "major"),
            ("refactor: update\n\nBREAKING CHANGE: new config", "major"),
            ("docs: update readme", None),
        ],
    )
    def test_get_mode(self, msg, expected):
        assert update_version.get_mode(msg) == expected

    def test_read_version(self, tmp_path):
        version_path = tmp_path / ".version"

        version_path.write_text("1.2.3\n")
        update_version.VERSION_FILE = version_path
        assert update_version.read_version() == "1.2.3\n"

        version_path.write_text("0.0.0-dev")
        with pytest.raises(ValueError):
            update_version.read_version()

    def test_write_version(self, tmp_path):
        version_path = tmp_path / ".version"
        update_version.VERSION_FILE = version_path
        version_path.write_text("0.0.0\n")

        new_version = "1.2.3"
        update_version.write_version(new_version)

        with version_path.open("r") as fp:
            written = fp.read()
            assert written == new_version + "\n"
