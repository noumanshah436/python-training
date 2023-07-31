# f = open("C:\\Users\\Syed Numan Rehman\\Desktop\\test.txt", "w")
# a = f.write("Nouman bhai bahut achhe hain\n")      # erase previous data
# print(a)
# f.close()

# f = open("C:\\Users\\Syed Numan Rehman\\Desktop\\test.txt", "a")
# a = f.write("Harry bhai bahut achhe hain\n")     # write data at the end of file
# print(a)
# f.close()


# Handle read and write both
# f = open("C:\\Users\\Syed Numan Rehman\\Desktop\\test.txt", "r+")
f = open("/home/dev/Desktop/test.txt", "r+")
print(f.read())
f.write("thank you")  # append text at the end just after the end of file char
