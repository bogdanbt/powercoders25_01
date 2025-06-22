import pytest
from sock_merchant import sock_merchant

@pytest.mark.socks
@pytest.mark.parametrize("socks, expected", [
    ([1, 2, 1, 2, 1, 3, 2], 2),
    ([10, 20, 20, 10, 10, 30, 50, 10, 20], 3),
    ([1, 1, 1, 1], 2),
    ([1, 2, 3, 4], 0),
    ([100]*100, 50),
    ([], 0),
])
def test_sock_merchant(socks, expected):
    assert sock_merchant(socks) == expected
