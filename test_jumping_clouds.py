import pytest
from jumping_clouds import jumping_on_clouds

@pytest.mark.jumping
@pytest.mark.parametrize("n, c, expected", [
    (7, [0, 0, 1, 0, 0, 1, 0], 4),
    (6, [0, 0, 0, 0, 1, 0], 3),
    (2, [0, 0], 1),
    (1, [0], 0),
    (3, [0, 1, 0], 1),
    (4, [0, 0, 1, 0], 2),
    (8, [0, 0, 0, 1, 0, 0, 1, 0], 4)
])
def test_jumping_on_clouds(n, c, expected):
    assert jumping_on_clouds(n, c) == expected
