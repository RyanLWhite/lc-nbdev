import pytest
from leetcode_solutions.problem_003_length_of_longest_substring import length_of_longest_substring as f


def test_empty_string():
    assert f("") == 0
