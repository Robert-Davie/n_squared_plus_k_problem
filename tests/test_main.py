from src.n_2_plus_k.main import get_largest_prime_factor, split_search_between_processes, check_p1, Settings, get_negative_even_squares_up_to
import pytest


@pytest.mark.parametrize("input_value, expected_result", [
    (20, 5),
    (100, 5),
    (111, 37),
    (33, 11),
    (194, 97),
    (97, 97),
    (0, None),
    (-6, 3),
])
def test_new_get_largest_prime_factor(input_value, expected_result):
    assert get_largest_prime_factor(input_value) == expected_result



# @pytest.mark.parametrize("input_value, expected_result", [
#     (20, 5),
#     (100, 5),
#     (111, 37),
#     (33, 11),
#     (194, 97),
#     (97, 97),
#     (0, None),
#     (-6, 3),
# ])
# def test_new_get_largest_prime_factor_v2(input_value, expected_result):
#     assert get_largest_prime_factor_v2(input_value) == expected_result


# fails on last one for some reason?
@pytest.mark.parametrize("given_n, expected", [
    (-1, []),
    (-4, [-4]),
    (-10, [-4]),
    (-8, [-4]),
    (-25, [-4, -16]),
    (-100, [-4, -16, -36, -64, -100]),
])
def test_get_negative_even_square_up_to(given_n, expected):
    assert get_negative_even_squares_up_to(given_n) == expected


@pytest.mark.parametrize("k, p1_candidate, expected_result", [
    (1, 89, (True, 233)),
    (1, 90, (False, None)),
    (1, 0, (False, None)),
    (-4, 11, (True, 13)),
    (3, 2089, (True, 10009))
])
def test_check_p1(k, p1_candidate, expected_result):
    assert check_p1(k, p1_candidate) == expected_result


@pytest.mark.parametrize("k, settings, expected_result", [
    (1, Settings(1, 1, 1, 100, 2, False), [(1, 89, 233)]),
    (2, Settings(2, 2, 500, 600, 2, False), [(2, 571, 2131)]),
])
def test_split_search_between_processes(k, settings, expected_result):
    assert split_search_between_processes(k, settings) == expected_result