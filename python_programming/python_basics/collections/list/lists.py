grocery = ["Harpic", "vim bar", "deodrant", "Bhindi",
           "Lollypop", 56]
# print(grocery[5])

numbers = [2, 7, 9, 11, 3]
print(numbers[0])
# print(max(numbers))
# print(min(numbers))
# print(len(numbers))

# numbers.remove(9)
# numbers.pop()
# numbers.sort()

# numbers = []
# numbers.reverse()
# numbers.append(1)
# numbers.append(72)
# numbers.append(5)
# numbers.insert(2, 67)

# *********************
# list slicing    #  for slicing see string directory in this project

# print(numbers[0:5])
# print(numbers[:])  # by default [start:end]
# print(numbers[1:5:2])
# print(numbers[1:5:-1])
# print(numbers[::-1])   # for -ve step, consider as it reverse the string and then read according to given step
# -step slicing only works fine with default value (start , end ) whether it is string or list
print(numbers[::-2])
# 3, 11, 9, 7, 2

# print(numbers)
# numbers[1] = 98
# print(numbers)
# Mutable - can change
# Immutable - cannot change
