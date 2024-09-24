"""
How to use function caching in Python?
Function caching is a way to improve the performance of code by storing the return values of the function.
Before the 3.2 updates of Python, we had to create a cache ourselves by storing the value in a variable or
by other such means. But in Python 3.2, there is a new update in the functools module of Python.
To use this module, we have to import it first.

import functools

We have been facilitated with the help of a decorator known as lru_cache.  Decorators are an essential part
of Python. Decorators in Python can be used for a variety of different purposes.

We have to pass maxsize as parameter with the decorator. maxsize is defined to tell the program how many function call
return values we want to store in the cache. It automatically stores the values for the latest number of calls.


FIFO means First In, First Out, i.e., consider elements strictly in arrival order.
LRU is Least Recently Used, the cache element that hasn't been used the longest time is evicted
    (on the hunch that it won't be needed soon)
"""
import time
from functools import lru_cache


# It will store returned value of 3 latest function calls and if any one out of these three is called again, then
# it will not execute it again, instead it will use its stored value

@lru_cache(maxsize=3)
def some_work(n):
    # Some task taking n seconds
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(2)
    print("Done... Calling again")
    some_work(3)    # as this function call is stored in cache, it will not executed again
    print("Called again")
