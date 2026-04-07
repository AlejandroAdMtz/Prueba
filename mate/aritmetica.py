def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """Returns the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def modulo(a, b):
    """Returns the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot perform modulo by zero")
    return a % b


def power(a, b):
    """Returns a raised to the power of b."""
    return a ** b
