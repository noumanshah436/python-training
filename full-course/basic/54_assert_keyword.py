# assert
# The assert keyword is used when debugging code.
#
# The assert keyword lets you test if a condition in your code returns True,
# if not, the program will raise an AssertionError.
#

def avg(marks):
    assert len(marks) != 0
    return sum(marks) / len(marks)


def assert_with_error_msg(marks):
    assert len(marks) != 0, "list is Empty"
    return sum(marks) / len(marks)


mark1 = [10, 11, 12]
print("avg of mark1 :", avg(mark1))

# mark1 = []
# print("avg of mark1 :", avg(mark1))

# mark1 = []
# print("avg of mark1 :", assert_with_error_msg(mark1))
# # AssertionError: list is Empty


# x = "hello"
# #if condition returns False, AssertionError is raised:
# assert x == "goodbye", "x should be 'hello'"

