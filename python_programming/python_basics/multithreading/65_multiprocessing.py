# *********************************
# Python multiprocessing
# *********************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    print("cpu count:", cpu_count())  # tells the number of CPU count (logical processors) available ,
    #                                   and we can create that number of processes, if we create more processes
    #                                   than CPU_count then it will take more time to complete a task

    a = Process(target=counter, args=(500000000,))  # 1billion = 100 crores = 1 Arab
    b = Process(target=counter, args=(500000000,))

    """
    for arguments we have to pass in a tuple , since we have only one argument to pass in,  
    to differentiate it from an expression we have to add a comma at the end
    """

    a.start()
    b.start()

    print("processing...")

    a.join()
    b.join()

    print("Done!")
    print("finished in:", time.perf_counter(), "seconds")


if __name__ == '__main__':
    main()

#
#  here we have divide our task (count upto 1billion ) in two parts, and it will now take less
#      time to complete compare to single process.
#  if i divide this task upto 4 processes(cpu_count) , it will take optimum time on my machine
#     to complete that task.
#     ****************

# finished in: 24.680523 seconds   for two processes
# finished in: 20.3830714 seconds  for four processes
# finished in: 20.5949934 seconds  for eight processes (more time because of context switching in 4 cpu)
