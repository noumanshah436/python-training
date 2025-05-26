# ****************************************************
# Python threading tutorial
# ****************************************************
# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive).
#             use multiprocessing (in parallel) with cpu bound processes

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading(multiple threads running concurrently but not truly in parallel)

import threading
import time


def eat_breakfast():
    time.sleep(3)   # sleep for 3 seconds
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")


def running_count(test_, string_):
    i = 0
    # print(type(test_), type(string_))
    print("argument received =", test_, string_)
    while i < 5:
        print("running threads =", threading.active_count())
        time.sleep(2)
        i += 1


# the main thread create 3 additional threads and run its remaining instruction after it (in case of no synchronization)

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

arg_list = [23, "hello"]
test = threading.Thread(target=running_count, args=arg_list)
test.start()


# thread synchronization:
# our calling thread(main thread) will wait around
# for another thread  to finish before it can move on with its own instruction set
x.join()
y.join()
z.join()

print(threading.active_count())  # return count of running threads
print(threading.enumerate())    # show list of running threads
print(time.perf_counter())      # performance_counter = how long our calling thread(main thread) takes
#                                                          to finish its sets of instructions

