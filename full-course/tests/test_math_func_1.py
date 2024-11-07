

import math_func

# For test function name should start with `test_`, else pytest will not run it

# https://www.youtube.com/watch?v=_QtM7QGuj1A&list=PLS1QulWo1RIaNFUz4zrztWlCJgkpXht-H&index=1&pp=iAQB


def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7


def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14


# pytest test_math_func_1.py -v