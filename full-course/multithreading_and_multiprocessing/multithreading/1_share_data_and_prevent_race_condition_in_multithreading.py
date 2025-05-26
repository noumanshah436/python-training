


from multiprocessing import Lock
import threading
import time

# share data between threads with a global variable (as threads shared the same data)
database_value = 0

def increase(lock):
    global database_value
    
    with lock:
        # critical section
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


def main():
    threads = []
    num_threads = 2
    lock = Lock()

    print(f"start value ------------------ {database_value}")

    for i in range(num_threads):
        t = threading.Thread(target=increase, args=(lock,))
        threads.append(t)

    # start threads
    for t in threads:
        t.start() 

    # join threads: wait for the threads to complete
    for t in threads:
        t.join()

    print(f"end value ------------------ {database_value}")


if __name__ == '__main__':
    main()
