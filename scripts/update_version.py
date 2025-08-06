# coding: utf-8
"""
Script to update the .version based on the commit message

MAJOR.MINOR.PATCH

MAJOR: BREAKING CHANGE
MINOR: feat
PATCH: fix

NO UPDATE: build, chore, docs, refactor, test
"""

import re
import sys
import pathlib
import logging
import subprocess

logger = logging.getLogger(__name__)

VERSION_FILE = pathlib.Path(".version")


def update(current_version: str, mode: str) -> str:
    """
    Update the version based on the mode:
    - patch
    - minor
    - major
    """
    version = re.search(
        r"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)", current_version
    )
    major, minor, patch = version.groups()

    match mode:
        case "major":
            return f"{int(major)+1}.0.0"
        case "minor":
            return f"{major}.{int(minor)+1}.0"
        case "patch":
            return f"{major}.{minor}.{int(patch)+1}"
        case _:
            raise KeyError(f"Unknown key {mode}")


def get_mode(message: str) -> str | None:
    """
    Determine the update mode based on the commit message
    """
    if re.search(r"(BREAKING CHANGE|!):\s", message):
        return "major"

    if re.match(r"(feat)(\(.+\))?:", message):
        return "minor"

    if re.match(r"(fix)(\(.+\))?:", message):
        return "patch"

    return None


def read_version() -> str:
    """
    Read the actual version store in version file
    """
    version = VERSION_FILE.read_text()

    if re.match(r"^((\d+).){2}\d+$", version):
        return version

    raise ValueError(
        "Versioning format doesn't match requirement - "
        f"{version} expected X.X.X number only"
    )


def write_version(new_version: str) -> None:
    """
    Write the new version in the version file
    """
    VERSION_FILE.write_text(new_version + "\n")


def main() -> None:
    """
    Update the version accordingly to the commit message
    """
    msg = subprocess.check_output(
        ["git", "log", "-1", "--pretty=%B"], text=True
    ).strip()
    mode = get_mode(msg)
    current_version = read_version()

    if mode:
        new_version = update(current_version, mode)
        write_version(new_version)
        logger.info(
            "Version updated - %s: %s > %s", mode.upper(), current_version, new_version
        )
    else:
        logger.info("Version not updated - %s", current_version)

    sys.exit(0)


if __name__ == "__main__":
    main()
