# text = "Yooooooooo\nThis is some text\nHave a good one!\n"

# with open('test.txt', 'w') as file:
#     file.write(text)

# **********************************

lst = "BSCSF18M001,Ali,5,3.5".split(",")
print(lst)
dic = {"Roll num": lst[0], "name": lst[1], "Sem": lst[2], "CGPA": lst[3]}
print(dic)


def file_writer(file_name):
    file = open(file_name, "w")
    strig = dic.values()
    string = ','.join(lst)
    file.write(dic)
    file.close()

file_writer("test.txt")

# def writeStudentRecord(filename, dictRec):
# 	file = open(filename, 'a')
# 	lst = dictRec.values()
# 	string = ','.join(lst)
# 	file.write(string)
# 	file.close()
