"""

What opening a file with "With block" actually does is to create a context manager that automatically
closes a file after processing it. Another benefit of using a “With block” is that we can open multiple
files in a single block by separating them using a comma. All the files could have different modes of opening.
 For example, we can access one file for reading and another one for writing purposes. Both files should have
 different objects referring to them.

The syntax would be:
With open(“file1txt”) as f, open(“file2.txt”) as g

Both files will be simultaneously closed together.

Let us once again briefly go over the advantages of With block:
Multiple files can be opened.
The files that are opened together can have different modes
Automatically closes file
Saves processing power by opening and closing file only when running code inside the block
Creates a context manager, so lesser chances of an exception occurring

"""


with open("test.txt") as f:
    a = f.readlines()
    print(a)

# f = open("harry.txt", "rt")
# Question of the day - Yes or No and why?
# f.close()

