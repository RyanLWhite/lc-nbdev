# Initial placeholder for the function
def length_of_longest_substring(s: str) -> int:
    """Finds the length of the longest substring without repeating characters."""
    substring_lengths = [0]  # there is always a substring of length zero

    # generate candidate_substring (as a list of chars)
    candidate_substring = []
    for el in s:
        if candidate_substring.count(el) > 0:
            # we were at the end of the substring before reaching el
            substring_lengths.append(len(candidate_substring))

            # prune everything up to previous instance of el from substring
            candidate_substring = candidate_substring[
                candidate_substring.index(el) + 1 :
            ]

        candidate_substring.append(el)

    substring_lengths.append(len(candidate_substring))

    return max(substring_lengths)
