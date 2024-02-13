import json
from functools import partial
from pathlib import Path

import jsonschema
import pytest

ROOT = Path(__file__).parent.parent.resolve()


@pytest.fixture
def validate():
    return partial(jsonschema.validate, format_checker=jsonschema.draft7_format_checker)


@pytest.fixture
def codes_schema():
    return json.loads(ROOT.joinpath("schemas/codes.schema.json").read_text())


@pytest.fixture
def codes_meta_schema():
    return json.loads(ROOT.joinpath("schemas/codes_meta.schema.json").read_text())


@pytest.fixture
def categories_schema():
    return json.loads(ROOT.joinpath("schemas/categories.schema.json").read_text())


@pytest.fixture
def metadata_schema():
    return json.loads(ROOT.joinpath("schemas/metadata.schema.json").read_text())


@pytest.fixture
def mock_schema_endpoints(
    requests_mock, codes_schema, codes_meta_schema, categories_schema, metadata_schema
):
    requests_mock.get(
        "https://wannier-developers.github.io/wannier-ecosystem-registry/schemas/v1/codes.schema.json",
        text=json.dumps(codes_schema),
    )
    requests_mock.get(
        "https://wannier-developers.github.io/wannier-ecosystem-registry/schemas/v1/metadata.schema.json",
        text=json.dumps(metadata_schema),
    )
    requests_mock.get(
        "https://wannier-developers.github.io/wannier-ecosystem-registry/schemas/v1/codes_meta.schema.json",
        text=json.dumps(codes_meta_schema),
    )
    requests_mock.get(
        "https://wannier-developers.github.io/wannier-ecosystem-registry/schemas/v1/categories.schema.json",
        text=json.dumps(categories_schema),
    )
