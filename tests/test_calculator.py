"""
Unit tests for the Calculator class.

Uses pytest framework for testing.
"""

import pytest
from src.calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""

    @pytest.fixture
    def calc(self):
        """Create a fresh Calculator instance for each test."""
        return Calculator()

    # Addition tests
    def test_add_positive_numbers(self, calc):
        """Test addition of two positive numbers."""
        assert calc.add(2, 3) == 5

    def test_add_negative_numbers(self, calc):
        """Test addition of two negative numbers."""
        assert calc.add(-2, -3) == -5

    def test_add_mixed_numbers(self, calc):
        """Test addition of positive and negative numbers."""
        assert calc.add(-2, 5) == 3

    def test_add_floats(self, calc):
        """Test addition of floating point numbers."""
        assert calc.add(2.5, 3.5) == 6.0

    def test_add_zero(self, calc):
        """Test addition with zero."""
        assert calc.add(5, 0) == 5

    # Subtraction tests
    def test_subtract_positive_numbers(self, calc):
        """Test subtraction of two positive numbers."""
        assert calc.subtract(10, 3) == 7

    def test_subtract_negative_result(self, calc):
        """Test subtraction resulting in negative number."""
        assert calc.subtract(3, 10) == -7

    def test_subtract_floats(self, calc):
        """Test subtraction of floating point numbers."""
        assert calc.subtract(5.5, 2.5) == 3.0

    # Multiplication tests
    def test_multiply_positive_numbers(self, calc):
        """Test multiplication of two positive numbers."""
        assert calc.multiply(4, 5) == 20

    def test_multiply_by_zero(self, calc):
        """Test multiplication by zero."""
        assert calc.multiply(100, 0) == 0

    def test_multiply_negative_numbers(self, calc):
        """Test multiplication of negative numbers."""
        assert calc.multiply(-3, -4) == 12

    def test_multiply_mixed_signs(self, calc):
        """Test multiplication with mixed signs."""
        assert calc.multiply(-3, 4) == -12

    # Division tests
    def test_divide_evenly(self, calc):
        """Test division that results in whole number."""
        assert calc.divide(20, 4) == 5

    def test_divide_with_remainder(self, calc):
        """Test division with decimal result."""
        assert calc.divide(7, 2) == 3.5

    def test_divide_by_zero_raises_error(self, calc):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_divide_negative_numbers(self, calc):
        """Test division of negative numbers."""
        assert calc.divide(-12, -3) == 4

    # Power tests
    def test_power_positive_exponent(self, calc):
        """Test power with positive exponent."""
        assert calc.power(2, 3) == 8

    def test_power_zero_exponent(self, calc):
        """Test power with zero exponent."""
        assert calc.power(5, 0) == 1

    def test_power_negative_exponent(self, calc):
        """Test power with negative exponent."""
        assert calc.power(2, -1) == 0.5

    # History tests
    def test_history_records_operations(self, calc):
        """Test that operations are recorded in history."""
        calc.add(1, 2)
        calc.multiply(3, 4)
        history = calc.get_history()
        assert len(history) == 2
        assert "1 + 2 = 3" in history[0]
        assert "3 * 4 = 12" in history[1]

    def test_clear_history(self, calc):
        """Test clearing operation history."""
        calc.add(1, 2)
        calc.subtract(5, 3)
        calc.clear_history()
        assert calc.get_history() == []

    def test_history_is_copy(self, calc):
        """Test that get_history returns a copy, not the original list."""
        calc.add(1, 2)
        history = calc.get_history()
        history.append("fake entry")
        assert len(calc.get_history()) == 1
