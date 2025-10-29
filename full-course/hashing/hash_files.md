Sure! Here's a **simple Python example** that shows how to **hash an image file** (like `.jpg`, `.png`) using **SHA3-256**.

---

### ✅ Example: Hash an image file with SHA3-256

```python
import hashlib

# Replace with your image path
file_path = "example_image.jpg"

# Open the image file in binary mode
with open(file_path, "rb") as f:
    image_bytes = f.read()

# Create a SHA3-256 hash object
hasher = hashlib.sha3_256()

# Update the hash with the file's content
hasher.update(image_bytes)

# Get the hexadecimal digest (hash)
image_hash = hasher.hexdigest()

print(f"SHA3-256 hash of the image: {image_hash}")
```

---

### 🔍 Output

For example, if you run this on a file named `dog.png`, it might print:

```
SHA3-256 hash of the image: 87ae3b1f0d36a4f4e9a4b73430b09ef4ecf9c75b5b5cc74251df87436fdfc920
```

---

### 🧠 Why This is Useful

* Detect duplicates even if filenames are different.
* Ensure image hasn’t been tampered with.
* Use hash as a **digital fingerprint** for the file.

---

Would you like an example using chunked reading (for large files)?



### can we re-generate  file using hash

No, you **cannot regenerate or reconstruct a file from its hash**.

---

### 🔐 Why?

A **hash** (like SHA3-256) is a **one-way function** — it transforms input data (like a file) into a fixed-length string of characters, but it **cannot be reversed**. Think of it like:

> 📦 File → 🎯 Hash
> ❌ Hash → File (impossible)

This is by design, for **security** and **integrity** checking.

---

### 📌 Example:

If you hash an image file and get:

```
"8c14d3a1d8e6be932fc9d2f0b3f189c31c8cb6c40d3d842a994..."
```

That string contains **no recoverable file content** — it’s like a fingerprint, not a blueprint.

---

### 🔐 What is a hash used for then?

* **Verifying integrity** of a file (has it changed?).
* **Detecting duplicates**.
* **Storing passwords securely** (e.g., in hashed form).
* **Blockchain/data verification**.

---

Would you like a visual or analogy to make this concept clearer?
