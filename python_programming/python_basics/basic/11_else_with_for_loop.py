"""
Syntax:

for x in n:
   #statements
 else:
   #statements


When we use else with for loop the compiler will only go into the else block of code
when two conditions are satisfied:

1) The loop normally executed without any error.
2) We are trying to find an item that is not present inside the list or
   data structure on which we are implementing our loop.

Except for these conditions, the program will ignore the else part of the program.
For example, if we are just partially executing the loop using a break statement,
then the else part will not execute. So, a break statement is a must if we do not
want our compiler to execute the else part of the code.

"""


khana = ["roti", "Sabzi", "chawal"]

for item in khana:
    if item == "rotiroll":
        break

else:
    print("Your item was not found")


# *******************************

for i in ['C','O','D','E']:
    print(i)
else:
    print("Statement successfully executed")