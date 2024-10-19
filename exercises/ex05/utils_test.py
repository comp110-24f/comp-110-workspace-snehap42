"""EX05: Utils Test"""

__author__ = "730740674"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_edge_case() -> None:
    "Function for edge case (empty list) of only evens"
    edge_input: list[int] = []
    assert only_evens(edge_input) == []  # returns empty list


def test_only_evens_use_case_1() -> None:
    "Function for first use case of only evens"
    use_input_1 = [3, 5, 2, 4]
    assert only_evens(use_input_1) == [2, 4]  # list has only evens


def test_only_evens_use_case_2() -> None:
    "Function for second use case of only evens"
    use_input_2 = [24, 6, 5, 8]
    assert only_evens(use_input_2) == [24, 6, 8]  # list has only evens


def test_sub_edge_case() -> None:
    "Function for edge case (start > end) of sub"
    assert sub([9, 67, 3, 2, 0, 4], 4, 3) == []  # returns empty list


def test_sub_use_case_1() -> None:
    "Function for first use case of sub"
    assert sub([6, 7, 8, 9, 10], 2, 4) == [8, 9]  # list has range


def test_sub_use_case_2() -> None:
    "Function for second use case of sub"
    assert sub([24, 6, 8, 9, 10], 0, 3) == [24, 6, 8]  # list has range


def test_add_at_index_edge_case() -> None:
    "Function for edge case (empty list) of add at index"
    input_list: list[int] = []
    add_at_index(input_list, 3, 0)
    assert input_list == [3]  # returns single value


def test_add_at_index_use_case_1() -> None:
    "Function for first use case of add at index"
    input_list: list[int] = [97, 84, 76, 34]
    add_at_index(input_list, 2, 2)
    assert input_list == [97, 84, 2, 76, 34]
    # list has new input at new int


def test_add_at_index_use_case_2() -> None:
    "Function for second use case of add at index"
    input_list: list[int] = [45, 67, 32, 16]
    add_at_index(input_list, 37, 1)
    assert input_list == [45, 37, 67, 32, 16]
    # list has new input at new int


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        add_at_index([89, 99, 109, 229], -2, 45)
        # an IndexError is raised for the case when the add_at_index
        # is given an <index_to_insert_num>
        # that is greater than the length of our <list_object>
