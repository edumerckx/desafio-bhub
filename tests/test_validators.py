import os
from unittest import mock

from src.validators import validate_varenvs


@mock.patch.dict(
    os.environ,
    {
        'GORULES_TOKEN': 'token-teste',
        'GORULES_URL': 'url-teste',
        'HTTP_PORT': '5000',
        'LOG_LEVEL': 'DEBUG',
    },
    clear=True,
)
def test_should_return_true():
    assert (validate_varenvs()) == True


@mock.patch.dict(
    os.environ,
    {
        'GORULES_TOKEN': '',
        'GORULES_URL': '',
        'HTTP_PORT': '',
        'LOG_LEVEL': '',
    },
    clear=True,
)
def test_should_return_false():
    assert (validate_varenvs()) == False
