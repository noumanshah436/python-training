import os

# on linux
path = "/home/dev/Desktop/test.txt"
# path = "/home/dev/Desktop"

# on windows
# path = "C:\\Users\\Syed Numan Rehman\\Desktop\\test.txt"
# path2= "C:\\Users\\Syed Numan Rehman\\Desktop"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist!")
