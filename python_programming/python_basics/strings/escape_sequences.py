# Escape sequences are helpful when you need to include special characters in your strings or when formatting text in a specific way.
#  They are denoted by a backslash \ followed by a specific character, and they have various uses within strings and other contexts.

# Here are some common escape sequences in Python:

# \n: Newline - Inserts a new line in the string.
# \t: Tab - Inserts a horizontal tab.
# \\: Backslash - Inserts a literal backslash.
# \': Single quote - Inserts a single quote character.
# \": Double quote - Inserts a double quote character.
# \r: Carriage return - Used mainly in Windows text files, rarely used in Python.
# \b: Backspace - Moves the cursor back one character.
# \f: Form feed - Moves the cursor to the next logical page.

# Newline and Tab
print("Hello\nWorld")
# Output:
# Hello
# World

print("Python\tProgramming")
# Output: Python   Programming

# Backslash
print("C:\\Users\\Username")
# Output: C:\Users\Username

# Single and Double quotes
print('He said, \'Hello!\'')
# Output: He said, 'Hello!'

print("She said, \"Hi!\"")
# Output: She said, "Hi!"

# Backspace
print("Hello\bWorld")
# Output: HellWorld
