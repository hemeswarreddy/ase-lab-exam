"""Basic arithmetic operations for a command-line calculator project."""


def add(first, second):
    """Return the sum of two numbers."""
    return first + second


def subtract(first, second):
    """Return the difference between two numbers."""
    return first - second


def multiply(first, second):
    """Return the product of two numbers."""
    return first * second


def divide(first, second):
    """Return the quotient of two numbers."""
    if second == 0:
        raise ValueError("Cannot divide by zero.")
    return first / second
