import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src")
    ),
)

from code_smells_example import (
    calculate_math_average,
    calculate_history_average,
    process_student,
)


def test_calculate_math_average():
    assert calculate_math_average([5, 7, 9]) == 7


def test_calculate_history_average():
    assert calculate_history_average([6, 8, 10]) == 8


def test_process_student():
    student = {
        "name": "Hector",
        "grades": [7, 8, 9]
    }

    process_student(student)