"""
Exercise 1: Divide
"""
def divide(a, b):
  """Divides two numbers, handling potential division by zero.

  Args:
    a: The numerator.
    b: The denominator.

  Returns:
    The quotient, or None if b is zero.
  """

  if b == 0:
    assert b==0
    return None
  else:
    assert b!=0
    return a / b

"""
Exercise 2: Factorial
"""
def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.
  """

  if n == 0:
    assert n==0
    return 1
  else:
    assert n>0 and type(n)==int
    return n * factorial(n - 1)

"""
Exercise 3: String Reverse
"""
def reverse_string(string):
    assert string==str
    """Reverses a given string.

    Args:
        string: A string to be reversed.

    Returns:
        The reversed string.
    """

    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    assert reversed_string!=string
    return reversed_string

"""
Exercise 4: Fibonacci
"""
def fibonacci(n):
  """Generates the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """

  assert type(n)==int or type(n)==float

  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    assert n>1
    return fibonacci(n - 1) + fibonacci(n - 2)

"""
Exercise 5: Email Validation
"""

import re

def is_valid_email(email):
  """Determines whether email is valid or not

  Args:
    email: The email to validate

  Returns:
    Boolean value if email is valid
  """

  assert email is not None

  email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+"

  assert type(re.match(email_regex, email) is not None)==bool
  return re.match(email_regex, email) is not None

 