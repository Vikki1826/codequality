"""
A simple calculator module demonstrating basic arithmetic operations.

This module is designed for CI/CD pipeline demonstration with code quality tools.
"""


class Calculator:
    """A calculator class that performs basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator with a history list."""
        self.history = []

    def add(self, a: float, b: float) -> float:
        """
        Add two numbers together.

        Args:
            a: First number
            b: Second number

        Returns:
            The sum of a and b
        """
        result = a + b
        self._record_operation(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """
        Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            The difference of a and b
        """
        result = a - b
        self._record_operation(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The product of a and b
        """
        result = a * b
        self._record_operation(f"{a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """
        Divide a by b.

        Args:
            a: Dividend
            b: Divisor

        Returns:
            The quotient of a divided by b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._record_operation(f"{a} / {b} = {result}")
        return result

    def power(self, base: float, exponent: float) -> float:
        """
        Raise base to the power of exponent.

        Args:
            base: The base number
            exponent: The exponent

        Returns:
            base raised to the power of exponent
        """
        result = base ** exponent
        self._record_operation(f"{base} ^ {exponent} = {result}")
        return result

    def _record_operation(self, operation: str) -> None:
        """Record an operation in history."""
        self.history.append(operation)

    def get_history(self) -> list:
        """
        Get the history of operations.

        Returns:
            List of operation strings
        """
        return self.history.copy()

    def clear_history(self) -> None:
        """Clear the operation history."""
        self.history = []


def main():
    """Demonstrate calculator usage."""
    calc = Calculator()

    print("Calculator Demo")
    print("-" * 30)

    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"20 / 4 = {calc.divide(20, 4)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")

    print("\nOperation History:")
    for entry in calc.get_history():
        print(f"  {entry}")


if __name__ == "__main__":
    main()
