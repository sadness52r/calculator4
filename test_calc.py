import pytest
from src.calc_methods import summ, sub


@pytest.mark.parametrize(
    ('a', 'b', 'res'), [
        (2, 3, 5),
        (0, 0, 0),
        (-4, 6, 2),
        (-8, -8, -16),
        (-25, 25, 0),
    ]
)
def test_summ(a, b, res):
    assert summ(a, b) == res


@pytest.mark.parametrize(
    ('a', 'b', 'res'), [
        (2, 3, -1),
        (0, 0, 0),
        (-4, 6, -10),
        (-8, -8, 0),
        (-25, 25, -50),
    ]
)
def test_sub(a, b, res):
    assert sub(a, b) == res
