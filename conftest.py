import pytest
from ptd.app import PtdApp


@pytest.fixture
def ptd_app():
    return PtdApp()
