import pytest
from leetcode_solutions.longest_substring_without_repeating_characters import Solution

@pytest.fixture
def solver():
    return Solution()

def test_empty_string(solver):
    assert solver.lengthOfLongestSubstring("") == 0
