# What types are iterable in python?
# Every thing that we can loop over in python is an iterable.
# Examples of iterables include all sequence types (such as list , str , and tuple )
# and some non-sequence types like dict , file objects, and objects of any classes you
# define with an __iter__() method or with a __getitem__() method that implements Sequence semantics.

# Iterable is not an iterator , it is an iterable(we can iterate it) for example string is an iterable
# because there is __iter__ or __getitem__() defined. But we can get its iterator by using __iter__()
# or iter() method and iterate it with __next__ method
#
# A number is not iterable and it has no defination of iter() method
#
# ______________________

# Iterator in Python is simply an object that can be iterated upon. An object which will
#    return data, one element at a time.
# Technically speaking, a Python iterator object must implement two special methods,
#    __iter__() and __next__(), collectively called the iterator protocol.

# An object is called iterable if we can get an iterator from it.
# Most built-in containers in Python like: list, tuple, string etc. are iterables.
# The iter() function (which in turn calls the __iter__() method) returns an iterator from them.
# ______________________

# for an iterator it must  implements two methods
# 1) __iter__   (return iterable object)
# 2) __next__   (return next item of iterable)

# ( call by obj_name.__iter__  or  iter(obj_name) )
# ( call by obj_name.__next__   or next(obj_name) )

# ______________________

# numbers = [1, 2, 3]
# print(dir(numbers))   #  dir method returns all the methods in objects

# ______________________

num_list = [1, 4, 9]

# iterate using iterable object
iter_obj = iter(num_list)
print(type(iter_obj))   # <class 'list_iterator'>

while True:
    try:
        element = next(iter_obj)
        print(element)
    except StopIteration:
        break

# iterate using for loop
#
# for i in num_list:
#     print(i)

