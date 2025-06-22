import pytest
from repeated_string import repeated_string

@pytest.mark.string
@pytest.mark.parametrize("s, n, expected", [
    ("a", 1000000, 1000000),
    ("abcac", 10, 4),
    ("aba", 10, 7),
    ("bcd", 10, 0),
    ("a", 0, 0),
    ("", 100, 0),
])
def test_repeated_string(s, n, expected):
    assert repeated_string(s, n) == expected
