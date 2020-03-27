import pytest
import random
from algorithms import SortingAlgorithms


@pytest.fixture
def algorithm_list():
    numbers = [random.randint(0, 100) for i in range(100)]
    return SortingAlgorithms(numbers)


def test_selection_sort(algorithm_list):
    assert algorithm_list.selection_sort() == sorted(algorithm_list.numbers)


def test_quick_sort(algorithm_list):
    assert algorithm_list.quick_sort(None) == sorted(algorithm_list.numbers)


def test_recursive_insertion_sort(algorithm_list):
    assert algorithm_list.recursive_insertion_sort(None, None) == sorted(algorithm_list.numbers)


def test_merge_sort(algorithm_list):
    assert algorithm_list.merge_sort() == sorted(algorithm_list.numbers)
