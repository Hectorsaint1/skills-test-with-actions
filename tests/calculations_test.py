# System Modules
import sys
import os
import math

# Installed Modules
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    radius = 1
    result = area_of_circle(radius)
    assert result == pytest.approx(math.pi)


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    n = 10
    result = get_nth_fibonacci(n)
    assert result == 55


def test_area_of_circle_negative_radius_raises():
    """Negative radius should raise ValueError."""
    with pytest.raises(ValueError):
        area_of_circle(-1)


def test_get_nth_fibonacci_negative_raises():
    """Negative n should raise ValueError."""
    with pytest.raises(ValueError):
        get_nth_fibonacci(-5)


def test_get_nth_fibonacci_large_index():
    """Test a larger Fibonacci index for correctness."""
    assert get_nth_fibonacci(20) == 6765
