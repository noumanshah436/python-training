"""
✅ What is a Process?
A process is an instance of a running program. Each process has its own memory space, code, data, and system 
resources. Each process can contain multiple threads. When you run a Python script, it runs in a process.

✅ What is Multiprocessing?
Multiprocessing is a Python module that allows you to create and run multiple processes in parallel. This is 
especially useful for CPU-bound tasks that benefit from using multiple cores of your CPU.

Python's Global Interpreter Lock (GIL) prevents multiple threads from executing Python bytecodes simultaneously. But 
using multiprocessing bypasses the GIL by running each process in its own Python interpreter with its own memory 
space, enabling true parallelism.

"""

from multiprocessing import Process, current_process
import os
import time

def square_numbers():
    process = current_process()
    print(f"Started process: {process.name} with PID {process.pid}")
    
    for i in range(100):
        _ = i + i  # Dummy operation
        time.sleep(0.1)

    print(f"Finished process: {process.name} with PID {process.pid}")

def main():
    processes = []                        
    num_processes = os.cpu_count()      # Get the number of available CPU cores

    for i in range(num_processes):      # Create a process for each CPU core
        p = Process(target=square_numbers)  # Create a new process to run square_numbers()
        processes.append(p)             # Add the process to the list

    for p in processes:
        p.start() # Start each process (they run in parallel)

    for p in processes:
        # Wait for all process to complete before continuing, 
        # this blocks the main program until these processes are finished
        p.join() 

    print('end main')

if __name__ == '__main__':
    main()