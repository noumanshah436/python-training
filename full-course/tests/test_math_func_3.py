import math_func
import pytest


# @pytest.mark.parametrize :
# allows you to run the test function multiple times with different arguments.
# This is particularly useful for testing multiple cases without duplicating code.

@pytest.mark.parametrize('num1, num2, result',
                         [
                             (7, 3, 10),
                             ('Hello', ' World', 'Hello World'),
                             (10.5, 25.5, 36)
                         ]
                         )
def test_add(num1, num2, result):
    assert math_func.add(num1, num2) == result


# Run tests:
# pytest test_math_func_3.py

# *********************************************

# The `parametrize` decorator takes two arguments:

#     1- **Argument names**: The first parameter (`'num1, num2, result'`) is a string listing the variable names used in each test case.

#     2- **Argument values**: The second parameter is a list of tuples, where each tuple represents a set of arguments and the expected result:
#       - `(7, 3, 10)`: Checks if `math_func.add(7, 3)` returns `10`.
#       - `('Hello', ' World', 'Hello World')`: Checks if `math_func.add('Hello', ' World')` returns `'Hello World'`.
#       - `(10.5, 25.5, 36)`: Checks if `math_func.add(10.5, 25.5)` returns `36`.


# *********************************************


# ### How It Works Together

# When `pytest` runs, it:
# - Loads this test function.
# - Uses the `parametrize` decorator to pass each tuple from the list of parameters (`num1, num2, result`) into `test_add`.
# - Calls `test_add` three times, once for each set of parameters.
# - If all assertions in `test_add` are true across all cases, the tests pass.
