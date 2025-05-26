from multiprocessing import Lock, Process, Value
import time

# How to share data between processes
# Hot to use Locks to prevent race conditions

def add_100(num, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            num.value += 1


def main():

    shared_number = Value('i', 0)
    lock = Lock()

    print(f"number at beginning is {shared_number.value}")

    p1 = Process(target=add_100, args=(shared_number,lock))
    p2 = Process(target=add_100, args=(shared_number,lock))

    p1.start()
    p2.start()

    print("processing...")

    p1.join()
    p2.join()

    print(f"number at end is {shared_number.value}")


if __name__ == '__main__':
    main()
