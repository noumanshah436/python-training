To **prevent race conditions** in Python threads, you use **thread synchronization tools** from the `threading` module — mainly:

---

## ✅ What is a **Race Condition**?

A **race condition** happens when **two or more threads access shared data at the same time**, and the result depends on the order of execution.

Example:
Two threads updating the same variable without coordination may cause **data corruption or unexpected results**.

---

## ✅ How to Prevent Race Conditions

### 🔐 1. Use **Locks (Mutex)**

The most common and safest way to prevent race conditions.

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # Only one thread can enter this block at a time
            counter += 1

threads = []
for _ in range(2):
    t = threading.Thread(target=increment)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Final counter:", counter)
```

🔹 **Why `with lock:`?**
It automatically acquires and releases the lock, making the code cleaner and safer (equivalent to `lock.acquire()` / `lock.release()`).

---

### 🧰 2. Use **RLock** (Reentrant Lock)

If the same thread needs to acquire the lock multiple times (e.g., in nested functions), use `threading.RLock`.

```python
rlock = threading.RLock()
```

---

### 🧱 3. Use **Condition** or **Semaphore** (Advanced Cases)

These are used when:

* You want threads to wait for certain conditions.
* You’re limiting access to a shared resource (e.g., only 3 threads at a time).

#### Example using `Semaphore`:

```python
sem = threading.Semaphore(3)  # Only 3 threads can run this block at once

def worker():
    with sem:
        # Critical section
        print(f"{threading.current_thread().name} is working")
        time.sleep(1)
```

---

## 🚫 What Happens Without a Lock?

```python
# Unsafe increment
counter = 0

def unsafe_increment():
    global counter
    for _ in range(100000):
        counter += 1

# This often gives incorrect results
```

Even though `counter += 1` looks simple, it's **not atomic** — it involves:

1. Reading `counter`
2. Adding 1
3. Writing back the value

If two threads interleave during these steps, you lose updates.

---

## ✅ Summary

| Tool        | Purpose                                      |
| ----------- | -------------------------------------------- |
| `Lock`      | Ensure only one thread accesses shared data  |
| `RLock`     | Reentrant version of Lock for nested use     |
| `Semaphore` | Limit concurrent access to a resource        |
| `Condition` | Wait/notify pattern for thread communication |

---

Let me know if you'd like a **visual simulation** or a **deadlock example** too!
