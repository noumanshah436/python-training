"""
print(value, ..., sep=' ', end=' ', file=sys.stdout, flush=False)


Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments: file: a file-like object (stream); defaults to the current sys.stdout.
sep: string inserted between values, default a space.
end: string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.

"""
import sys

print("print line ", end="\n")
print("This is an Error ", end="\n", file=sys.stderr)
print(1, 2, 3, 4, sep="*")
print(1, 2, 3, 4, sep=", ")

# ****************
a = 5

print("value of a is ", a)
# print("value of a is "+ a)    # error

print("value of a is " + str(a))
print(f"value of a is {a}")
print(type(f"value of a is {a}"))  # <class 'str'>
