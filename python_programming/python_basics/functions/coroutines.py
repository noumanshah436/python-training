# coroutine = is a function which can pause and resume its executoin

# Coroutines:-
# Coroutines are mostly used in cases of time-consuming programs, such as tasks related to machine learning
# or deep learning algorithms or in cases where the program has to read a file containing a large number of
# data. In such situations, we do not want the program to read the file or data, again and again, so we use
# coroutines to make the program more efficient and faster. Coroutines run endlessly in a program because
# they use a while loop with a true or 1 condition so it may run until infinite time. Even after yielding
# the value to the caller, it still awaits further instruction or calls. We have to stop the execution of
# coroutine by calling coroutine.close() function. It is very crucial to close a coroutine because its
# continuous running can take up memory space as we have discussed in Tutorial #75, related to function
# caching. We can define a coroutine using the following statements.
#
# def myfunc():
#     while True:
#         value = (yield)

# The while block continues the execution of the coroutine for as long as it receives values.
# The value is collected through the yield statement.

# ***********************************
# def myfunc():
#     print("Code With Harry")
#     while True:
#         value = (yield)
#         print(value)
#
#
# coroutine = myfunc()
# next(coroutine)
# coroutine.send("Python")
# # coroutine.send(" Tutorial ")
# coroutine.close()
#

# *******************************************
import time


def searcher():

    # Some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)
    print("Hello")

    while True:  # code before while loop only execute at next() statement
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")


search = searcher()
next(search)
search.send("harry")       # for send() stat,  while loop execute single iteration
search.send("Nouman")
search.send("harry and")

search.close()
