# Celery with Redis

Celery is a simple, flexible, and reliable distributed task queue used to process background jobs asynchronously.

Redis is commonly used as the message broker for Celery.

---

# Step 1 — Run Redis with Docker

Start a Redis container using Docker:

```bash
docker run -d -p 6379:6379 redis
```

Verify Redis is running:

```bash
docker ps
```

---

# Step 2 — Install Celery and Redis Dependencies

Install Celery with Redis support:

```bash
pip install -U "celery[redis]"
```

---

# Step 3 — Create a Celery Application

Create a file named `tasks.py`.

## `tasks.py`

```python
from celery import Celery

# Create Celery app
app = Celery(
    "tasks",
    broker="redis://localhost:6379/0"
)

# Create a task
@app.task
def exponent(x, y):
    return x ** y
```

### Explanation

* `Celery(...)` creates the Celery application.
* `broker` specifies Redis as the message broker.
* `@app.task` converts a normal Python function into a Celery task.

---

# Step 4 — Start the Celery Worker

Run the worker server:

```bash
celery -A tasks worker --loglevel=INFO
```

### Explanation

* `-A tasks` → loads the `tasks.py` module
* `worker` → starts the Celery worker
* `--loglevel=INFO` → shows task logs and events

---

# Step 5 — Execute a Task

Open another terminal and run Python:

```python
from tasks import exponent

result = exponent.delay(3, 4)

print(result.id)
```

### Output

```python
39f0d5e5-8c44-4c1e-a9a2-xxxxxxxxxxxx
```

The task is sent to Redis, and the Celery worker processes it asynchronously.

---

# Step 6 — Get the Task Result

```python
from tasks import exponent

result = exponent.delay(3, 4)

print(result.get())
```

### Output

```python
81
```

---

# Flower — Celery Monitoring Dashboard

Flower is a web-based monitoring tool for Celery.

It provides:

* Real-time task monitoring
* Worker status
* Task history
* Queue inspection
* Task performance metrics

---

# Step 7 — Install Flower

```bash
pip install flower
```

---

# Step 8 — Start Flower

Run:

```bash
celery -A tasks.app flower
```

or

```bash
celery -A tasks flower
```

---

# Step 9 — Enable Task Events

Start the Celery worker with task events enabled:

```bash
celery -A tasks worker --loglevel=INFO -E
```

### Explanation

* `-E` enables task event monitoring for Flower.

---

# Step 10 — Access Flower Dashboard

Open in browser:

```text
http://0.0.0.0:5555/
```

or

```text
http://localhost:5555/
```

---

# Project Structure

```text
project/
│
├── tasks.py
└── requirements.txt
```

---

# Complete Workflow

1. Start Redis
2. Start Celery worker
3. Send tasks using `.delay()`
4. Monitor tasks using Flower

---

# Useful Commands

## Check Running Containers

```bash
docker ps
```

## Stop Redis Container

```bash
docker stop <container_id>
```

## Start Worker with Events

```bash
celery -A tasks worker --loglevel=INFO -E
```

## Start Flower

```bash
celery -A tasks flower
```

---

# Requirements

## `requirements.txt`

```text
celery[redis]
flower
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

# Summary

This setup allows you to:

* Run background tasks asynchronously
* Use Redis as a broker
* Process jobs using Celery workers
* Monitor everything using Flower

Common use cases:

* Sending emails
* Background processing
* Scheduled jobs
* Notifications
* File processing
* Data pipelines
