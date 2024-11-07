import math_func
import pytest
import sys


# https://www.youtube.com/watch?v=VKY-0LEmrwk&list=PLS1QulWo1RIaNFUz4zrztWlCJgkpXht-H&index=3

@pytest.mark.skipif(sys.version_info < (3, 3), reason="do not run number add test")
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    print(math_func.add(7, 3), '-----------------------------------')


@pytest.mark.mark1
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10


@pytest.mark.mark2
def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Hello' in result


@pytest.mark.skip(reason="do not run number product test")
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result


# ************************************

# run all test of mark1
# pytest test_math_func_2.py -m mark1

# pytest test_math_func_2.py -m mark2

# ************************************

# sys package give the information about the Python version being used:

# $ python
# Python 3.12.3 (main, Jul 13 2024, 02:24:52) [GCC 11.4.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import sys
# >>> sys.version_info
# sys.version_info(major=3, minor=12, micro=3, releaselevel='final', serial=0)
# >>>

# ************************************


# sys.version_info < (3, 3)
# skip test if python version is less than 3.3
