from lib.time_error import *
from unittest.mock import Mock

def test_find_error():
    requests_mock = Mock()
    response_mock = Mock()
    requests_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime":1712849878.500285}
    time_mock = Mock()
    time_mock.time.return_value = 1712849879.500285
    timer_error = TimeError(requests_mock, time_mock)
    assert timer_error.error() == -1
