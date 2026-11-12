import pytest

from tests.mocks.source_mock import MOCK_SOURCE, MOCK_SOURCES


@pytest.fixture()
def mock_source():
    return MOCK_SOURCE.copy()

@pytest.fixture()
def mock_source_list():
    return MOCK_SOURCES.copy()