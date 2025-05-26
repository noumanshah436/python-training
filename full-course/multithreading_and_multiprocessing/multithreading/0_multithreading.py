"""
✅ What is a Thread?
A thread is the smallest unit of execution within a process.
A process can have multiple threads, all running in the same memory space.
Threads share the same memory and data of the parent process.
Threads are often used to perform tasks concurrently ((multiple threads running concurrently but not truly in parallel)).

✅ What is Multithreading?
Multithreading is a technique where multiple threads run within the same process, either simultaneously or in quick succession (concurrently).

🔸 Use Cases:
    Ideal for I/O-bound tasks like:
    File reading/writing
    Network requests
    Database access
    Not efficient for CPU-bound tasks in Python due to the Global Interpreter Lock (GIL).

✅ What is the Global Interpreter Lock (GIL)?
The GIL is a mutex (lock) used in the CPython interpreter to prevent multiple native threads from executing Python bytecodes at once.
Prevents true parallel execution of threads for CPU-bound tasks.
Only one thread can execute Python code at a time, even on multi-core machines.
Workaround for CPU-bound tasks: use multiprocessing instead.
"""


import threading
import time


def square_numbers():
    thread = threading.current_thread()
    print(f"Started thread: {thread.name}")

    for i in range(100):
        _ = i + i  # Dummy operation
        time.sleep(0.1)
    print(f"Finished thread: {thread.name}")


def main():
    threads = []
    num_threads = 4  # You can change this number as needed

    print(f"Creating {num_threads} threads")

    for i in range(num_threads):
        t = threading.Thread(target=square_numbers, name=f'Worker-{i+1}')
        threads.append(t)

    # start threads
    for t in threads:
        t.start()

    # join threads: wait for the threads to complete
    for t in threads:
        t.join()

    print('All threads completed. End of main.')


if __name__ == '__main__':
    main()
