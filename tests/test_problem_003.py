# import pytest
from leetcode_solutions.problem_003 import length_of_longest_substring


# Initial placeholder test (will fail because of NotImplementedError)
# def test_placeholder():
#     with pytest.raises(NotImplementedError):
#         length_of_longest_substring(1)


def test_empty_string():
    assert length_of_longest_substring("") == 0


def test_single_char():
    assert length_of_longest_substring("a") == 1
    assert length_of_longest_substring(" ") == 1


def test_all_unique_chars():
    assert length_of_longest_substring("abcde") == 5
    assert length_of_longest_substring("abcde ") == 6


def test_my_tests():
    assert length_of_longest_substring("aaa") == 1
    assert length_of_longest_substring("aab") == 2
    assert length_of_longest_substring("aba") == 2
    assert length_of_longest_substring("abcde") == 5
    assert length_of_longest_substring("abcde ") == 6
    assert length_of_longest_substring("abcdeaaa ") == 5
