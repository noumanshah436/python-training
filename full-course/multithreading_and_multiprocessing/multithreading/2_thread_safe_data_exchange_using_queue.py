"""
How to use a Queue for thread safe data exchanges?

Using a Queue is one of the best and safest ways to exchange data between threads in Python.

Python's queue.Queue is thread-safe by design — it uses internal locks to handle synchronization, 
so you don't need to use locks manually.

✅ Why Use Queue for Threads?
Built-in thread safety ✅
Easy communication between producer/consumer threads ✅
Avoids race conditions ✅

"""
import threading
import queue
import time

# Create a thread-safe queue
q = queue.Queue()

# Producer function
def producer():
    for i in range(5):
        item = f"item-{i}"
        print(f"[Producer] Producing {item}")
        q.put(item)  # Thread-safe enqueue
        time.sleep(1)

# Consumer function
def consumer():
    while True:
        item = q.get()  # Thread-safe dequeue (blocks if empty)
        if item is None:
            break  # Sentinel value to stop the thread
        print(f"[Consumer] Consuming {item}")
        time.sleep(2)
        q.task_done()  # Signal task completion

# Start the threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

# Wait for the producer to finish
producer_thread.join()


# Signal the consumer to stop by sending a sentinel value
q.put(None)
consumer_thread.join()

print("All tasks completed.")


"""

### 🔍 How It Works

| Part            | Purpose                                                   |
| --------------- | --------------------------------------------------------- |
| `q.put(item)`   | Adds item to the queue (from producer)                    |
| `q.get()`       | Retrieves item from queue (by consumer), blocks if empty  |
| `q.task_done()` | Tells the queue the task is complete (used with `join()`) |
| `q.join()`      | Waits until all items are processed (optional)            |
| `q.put(None)`   | Special "sentinel" value to signal consumer to exit       |

---

## ✅ Use Cases

* **Producer-Consumer Pattern**
* Thread-safe logging
* Background workers
* Thread pool task queues

---

## 🛠 Other Types of Queues

| Queue Type              | Description                                              |
| ----------------------- | -------------------------------------------------------- |
| `queue.Queue()`         | FIFO (First-In First-Out) — default                      |
| `queue.LifoQueue()`     | LIFO (Last-In First-Out) — like a stack                  |
| `queue.PriorityQueue()` | Orders items by priority using `(priority, item)` tuples |

---

## ✅ Summary

* `queue.Queue` handles **locking and synchronization for you**.
* Ideal for **communication and data sharing** between threads.
* Avoids the need to manually manage **locks or race conditions**.

"""

# *******************************************************************************************

"""

### ✅ Why `q.task_done()` is used

`q.task_done()` is used to **tell the queue that a task retrieved with `q.get()` has been fully processed**.

---

### 🔍 When to use it:

Whenever you call `q.get()` to retrieve an item from the queue, and you're **done processing that item**, you should call:

```python
q.task_done()
```

---

### 💡 What happens if you don't call `q.task_done()`?

* If you're using `q.join()` to **wait for all tasks to be completed**, it will **never return** if `task_done()` isn't called for each `get()`.
* You'll create a **logical deadlock** — the program will hang, thinking some tasks are still running.

---

### 🔄 Typical Workflow:

```python
item = q.get()     # Block until item is available
# process the item ...
q.task_done()      # Mark this item as done
```

Then in the main thread (or producer), you might do:

```python
q.join()  # Wait until all items have been marked as done
```

---

### ✅ Full Example (with `q.join()`):

```python
import threading
import queue
import time

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Processing {item}")
        time.sleep(1)
        q.task_done()

# Add items to the queue
for i in range(5):
    q.put(f"task-{i}")

# Start worker thread
t = threading.Thread(target=worker)
t.start()

# Wait for all tasks to be processed
q.join()
print("All tasks are complete.")

# Stop the worker
q.put(None)
t.join()
```

---

### 🧠 Summary

| Function        | Purpose                                        |
| --------------- | ---------------------------------------------- |
| `q.get()`       | Takes an item from the queue                   |
| `q.task_done()` | Says "I'm done processing this item"           |
| `q.join()`      | Blocks until all items have been `task_done()` |

Let me know if you'd like to explore **queue with multiple workers** next!



"""