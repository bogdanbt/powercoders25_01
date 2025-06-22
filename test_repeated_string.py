import pytest
from repeated_string import repeated_string

@pytest.mark.string
@pytest.mark.parametrize("s, n, expected", [
    ("a", 1000000, 1000000),     
    ("abac", 10, 5),               
    ("aba", 10, 7),               
    ("bcd", 10, 0),                
    ("a", 0, 0),                   
    ("", 100, 0),                  
    ("a", 1, 1),                   
    ("b", 1, 0),                   
    ("abc", 1, 1 if "a" in "abc"[0] else 0),  
    ("a", 1000000000000, 1000000000000),    
])
def test_repeated_string(s, n, expected):
    assert repeated_string(s, n) == expected
