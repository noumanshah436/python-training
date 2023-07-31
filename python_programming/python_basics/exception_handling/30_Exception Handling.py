# exception =   events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:     # (as e) cath the exception , optional but good
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:     # execute if there is no exception
    print(result)
finally:   # always comes at the end and it always execute wheather or not we catch an exception
    print("This will always execute")
