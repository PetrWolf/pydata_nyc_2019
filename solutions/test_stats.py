import pytest
from hypothesis import given
from hypothesis.strategies import lists, integers
from .stats import second_largest


def test_example():
    """Example based tests.

    With poorly chosen examples"""
    assert 4 == second_largest([1, 2, 3, 4, 5])
    assert 3 == second_largest([1, 2, 3, 4])


@given(values=lists(integers()))
def test_hypothesis(values):
    """Property based tests."""
    distinct_values = set(values)
    if len(distinct_values) > 1:
        # valid usage -> test expected properties
        v = second_largest(values)
        # returned value is present in the list
        assert v in values  
        # there is exactly one value greater than v
        assert 1 == len([x for x in distinct_values if x > v]) 
    else:
        # invalid usage -> test expected outcome
        with pytest.raises(ValueError):
            second_largest(values)
