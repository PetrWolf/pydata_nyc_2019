from typing import List

def second_largest(values: List[int]) -> int:
    """Returns the 2nd largest value from a given list."""
    try:
        return sorted(set(values))[-2]
    except IndexError:
        raise ValueError("second_largest() needs at least two distinct values")
