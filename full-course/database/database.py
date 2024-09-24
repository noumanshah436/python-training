import pymysql

# connect at different port
# https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
# https://pymysql.readthedocs.io/en/latest/modules/connections.html

"""
conn = pymysql.connect(host="localhost",
                       user="root",
                       passwd="",
			port="3307",
                       db="bcs")

"""

conn = pymysql.connect(host="localhost",
                       user="root",
                       passwd="",
                       db="bcs")

myCursor = conn.cursor()  # Create a new cursor to execute queries with

myCursor.execute("select * from students")  # Execute a query

# result = myCursor.fetchall()          # fetch all table records as tuple of tuples
# print(result[0], end="\n")
# # print(type(result[0]), end="\n")


# result = myCursor.fetchone()            # fetch one records as tuple and get each of its attributes
# print("ID :" + result[0], "    Name :" + result[1], "    City :" + result[2] + "   Gender :" + result[3])

result_all = myCursor.fetchall()
for rec in result_all:
    print("ID :" + str(rec[0]), "    Name :" + rec[1], "    City :" + rec[2], "     Gender :" + rec[3])

#

conn.commit()  # Commit changes to stable storage.
conn.close()
