import pytest
from counting_valleys import counting_valleys

@pytest.mark.counting
@pytest.mark.parametrize("n, s, expected", [
    (8, "UDDDUDUU", 1),
    (12, "DDUUDDUDUUUD", 2),
    (10, "UUUUDDUUDD", 0),
    (10, "DUDUDUDUDU", 5),
    (5, "DDDDD", 1),
    (5, "UUUUU", 0),
    (2, "DU", 1),
    (2, "UD", 0),
    (0, "", 0),
])
def test_counting_valleys(n, s, expected):
    assert counting_valleys(n, s) == expected
