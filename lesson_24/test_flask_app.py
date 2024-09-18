import pytest
from lesson_24.homework_24 import TestRequests
from lesson_24.data_logger import log


@pytest.fixture(scope='class')
def auth_token():
    test_requests = TestRequests()
    is_authenticated = test_requests.test_auth()
    if is_authenticated:
        yield test_requests.token
    else:
        pytest.fail("Authentication failed")


@pytest.mark.parametrize(
    "sort_by, limit, expected_status_code", [
        ('price', 5, 200),
        ('year', 3, 200),
        ('engine_volume', 7, 200),
        ('brand', 10, 200),
        ('nonexistent_field', 5, 200),
        (None, 5, 200),
        ('price', None, 200)
    ]
)
def test_get_cars(auth_token, sort_by, limit, expected_status_code):
    test_requests = TestRequests()
    test_requests.token = auth_token
    params = {}
    if sort_by:
        params['sort_by'] = sort_by
    if limit:
        params['limit'] = limit
    response = test_requests.test_cars(**params)
    log.info(f"Test with sort_by: {sort_by}, limit: {limit}, expected_status_code: {expected_status_code}")
    assert response['status_code'] == expected_status_code
    log.info(f"Received status code: {response['status_code']} - Test Passed")

