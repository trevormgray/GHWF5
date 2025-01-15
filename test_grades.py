
from grades import compute_hw_average


def test_zero_grades():
    grades = []
    assert compute_hw_average(grades) == 0


def test_single_grade():
    grades = [42]
    assert compute_hw_average(grades) == 42

def test_multiple_grades():
    grades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert compute_hw_average(grades) = 5.5
