import pymysql

# we can use """ for multilines string   (don't worry for spacing or indentation while writing sql in string)

conn = pymysql.connect(host="localhost",
                       user="root",
                       passwd="",
                       db="bcs")

myCursor = conn.cursor()

""" create table"""
# myCursor.execute("""create table names
#     (
#         id int primary key ,
#         name varchar(25)
#     )
#     """)

""" insert records in table table"""
# myCursor.execute("insert into names(id,name) values(2,'Ali')")
# myCursor.execute("insert into names(id,name) values(1,'Nouman')")
# myCursor.execute("insert into names(id,name) values(3,'Naeem')")

"""delete record"""
# myCursor.execute("delete from names where id=3")

"""update record"""
myCursor.execute("""update names 
                    set name='Farhan'
                    where id =1 """)

"""  fetch and display records"""
# print(myCursor.fetchall(), end="\n")

# result = myCursor.fetchone()
# print("ID :" + result[0], "    Name :" + result[1], "    City :" + result[2] + "   Gender :" + result[3])

# result_all = myCursor.fetchall()
# for rec in result_all:
#     print("ID :" + rec[0], "    Name :" + rec[1], "    City :" + rec[2] + "     Gender :" + rec[3])

#


conn.commit()
conn.close()
