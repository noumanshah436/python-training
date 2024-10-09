

# **`enumerate()`**: Adds a counter to an iterable, returning tuples of (index, value).
names = ['Alice', 'Bob', 'Charlie']
result = list(enumerate(names, start=1))
print(result)  # Output: [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')]


# **`reversed()`**: Returns the elements of a sequence in reverse order.
numbers = [1, 2, 3, 4]
result = list(reversed(numbers))
print(result)  # Output: [4, 3, 2, 1]

#  **`sorted()`**: Returns a sorted list from an iterable.
names = ['Charlie', 'Alice', 'Bob']
result = sorted(names)
print(result)  # Output: ['Alice', 'Bob', 'Charlie']
