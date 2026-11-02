import pytest
from attendance import attendance


@pytest.mark.parametrize("present, total, expected", [
    (5, 10, 50.0),
    (0, 10, 0.0),
    (10, 10, 100.0),
    (3, 0, 0.0)
])
def test_attendance(present, total, expected):
    assert attendance(present, total) == expected
