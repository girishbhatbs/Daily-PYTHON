def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    return a**b


def factorial(n):
    if n < 0:
        raise ValueError("Cannot compute factorial of negative number")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


result = add(5, 3)
print(f"Addition: {result}")
result = subtract(5, 3)
print(f"Subtraction: {result}")
result = multiply(5, 3)
print(f"Multiplication: {result}")
result = divide(5, 3)
print(f"Division: {result}")
result = power(5, 3)
print(f"Power: {result}")
result = factorial(5)
print(f"Factorial: {result}")


# Test cases
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0


def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    try:
        divide(5, 0)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError not raised"
