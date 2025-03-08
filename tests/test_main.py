from src.n_2_plus_k.main import get_largest_prime_factor
import pytest


@pytest.mark.parametrize("input_value, expected_result", [
    (20, 5),
    (100, 5),
    (111, 37),
    (33, 11),
    (194, 97),
    (97, 97)
])
def test_new_get_largest_prime_factor(input_value, expected_result):
    assert get_largest_prime_factor(input_value) == expected_result