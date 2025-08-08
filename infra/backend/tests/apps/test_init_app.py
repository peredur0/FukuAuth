# coding: utf-8
"""
Tests for function in the init applications
"""

import json
import pytest

from infra.backend.apps.init_app import main


@pytest.fixture
def collection_in_file(tmp_path):
    schema_file = tmp_path / "collection_1.json"
    data = {
        "name": "",
        "indexes": {"field_1": {"unique": True}},
        "$jsonSchema": {
            "bsonType": "object",
            "required": [],
            "properties": {
                "field_1": {"bsonType": "string", "description": "field_1 desc"},
                "field_2": {"bsonType": "date", "description": "field_2 desc"},
                "field_3": {"enum": ["a", "b", "c"], "description": "field_3 desc"},
            },
        },
    }
    with schema_file.open("w") as fp:
        json.dump(data, fp)

    return schema_file


class TestInitApp:

    def test_check_new_collection(self, collection_in_file):
        main.check_collection(collection_in_file)
        assert 1 == 1
