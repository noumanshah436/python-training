In Python, **encoding** and **decoding** deal with converting between **strings (`str`)** and **bytes (`bytes`)** — which is essential when working with files, network data, or any binary input/output.

---

## 🔁 Basics

* `encode("utf-8")` → converts a string to bytes
* `decode("utf-8")` → converts bytes back to a string

---

## 🧪 Example

```python
text = "Hello, world! 👋"

# Encode to bytes
encoded = text.encode("utf-8")
print(encoded)  # b'Hello, world! \xf0\x9f\x91\x8b'

# Decode back to string
decoded = encoded.decode("utf-8")
print(decoded)  # Hello, world! 👋
```

---

## ⚠️ Common Mistake

If you try to decode a string directly (instead of bytes), you'll get an error:

```python
text = "Hello"
text.decode("utf-8")  # ❌ AttributeError: 'str' object has no attribute 'decode'
```

✅ Fix:

```python
text.encode("utf-8").decode("utf-8")
```

---

## 🧠 Why It Matters

* File I/O: Reading/writing text files in various encodings (`utf-8`, `latin-1`, etc.)
* APIs: Encoding JSON, form data, or binary uploads
* Cryptography: Hashing or signing often works with bytes, not strings

---




Would you like examples involving file reading/writing or Base64 encoding/decoding as well?


## **File reading/writing** with encoding/decoding and also look at **Base64** encoding/decoding examples.


## 📁 1. **File Encoding and Decoding (Text Files)**

### ✅ Write a UTF-8 encoded text file:

```python
text = "سلام دنیا! Hello world!"

with open("hello.txt", "w", encoding="utf-8") as f:
    f.write(text)
```

### ✅ Read it back:

```python
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)  # سلام دنیا! Hello world!
```

---

## 🧾 2. **Working with Bytes (Binary Files)**

Let's say you have an image and want to read it as bytes:

```python
with open("image.jpg", "rb") as f:
    image_bytes = f.read()

print(type(image_bytes))  # <class 'bytes'>
```

Now you can hash it, encode it, or send it over a network.

---

## 🔐 3. **Base64 Encoding and Decoding**

Base64 is a way to convert binary data into text — useful when sending files over text-only protocols (like JSON or HTML).

### ✅ Encode image to Base64:

```python
import base64

with open("image.jpg", "rb") as image_file:
    image_bytes = image_file.read()

base64_string = base64.b64encode(image_bytes).decode("utf-8")
print(base64_string[:100])  # Just showing first 100 chars
```

### ✅ Decode it back and save:

```python
decoded_bytes = base64.b64decode(base64_string)

with open("restored.jpg", "wb") as f:
    f.write(decoded_bytes)
```

---
Here's your updated ✅ **Summary Table** with a "Usage" column explaining when and why each function is used:

---

## ✅ Summary

| Operation          | Method                  | Example                                   | Usage                                                                                      |
| ------------------ | ----------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------ |
| Encode str → bytes | `text.encode("utf-8")`  | `"hi".encode("utf-8")`                    | Converts a string to bytes for storage, transmission, or hashing.                          |
| Decode bytes → str | `b.decode("utf-8")`     | `b"hi".decode("utf-8")`                   | Converts byte data back to string for display or processing.                               |
| Read text file     | `"r", encoding="utf-8"` | `open("file.txt", "r", encoding="utf-8")` | Reads a text file in human-readable format, using UTF-8 encoding.                          |
| Read binary file   | `"rb"`                  | `open("image.jpg", "rb")`                 | Reads a file as raw bytes (e.g. images, PDFs) for processing/upload.                       |
| Base64 encode      | `base64.b64encode()`    | `base64.b64encode(b)`                     | Encodes binary data to Base64 so it can be sent over text-based formats like JSON or HTML. |
| Base64 decode      | `base64.b64decode()`    | `base64.b64decode(s)`                     | Decodes Base64 string back into raw bytes to save or use as a file.                        |

---


## Encoding a text file to Base64 and sending it as a JSON payload:


Let’s walk through **how to encode a text file to Base64 and send it as a JSON payload**, step by step:

## ✅ Step 1: Create a text file

Let's first create a file named `sample.txt`:

```python
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Hello, this is a Base64 test!")
```

---

## ✅ Step 2: Encode file content to Base64

```python
import base64
import json

# Read the file as bytes
with open("sample.txt", "rb") as f:
    file_bytes = f.read()

# Encode to Base64
base64_encoded = base64.b64encode(file_bytes).decode("utf-8")

# Prepare JSON payload
payload = {
    "filename": "sample.txt",
    "content_base64": base64_encoded
}

# Convert to JSON string
json_payload = json.dumps(payload, indent=2)

print(json_payload)
```

**Example Output:**

```json
{
  "filename": "sample.txt",
  "content_base64": "SGVsbG8sIHRoaXMgaXMgYSBCYXNlNjQgdGVzdCE="
}
```

---

## ✅ Step 3: Decode Base64 and save it back to file

This simulates receiving the JSON and restoring the file:

```python
# Decode the Base64 string back to bytes
decoded_bytes = base64.b64decode(payload["content_base64"])

# Save to a new file
with open("restored_sample.txt", "wb") as f:
    f.write(decoded_bytes)
```

Now, `restored_sample.txt` will contain the exact same content as `sample.txt`.

---

## ✅ Example: Base64 Encode and Decode an Image File (`image.png`)

### 🔹 Step 1: Encode the image to Base64

```python
import base64
import json

# Read the image as bytes
with open("image.png", "rb") as f:
    image_bytes = f.read()

# Encode to Base64
encoded_image = base64.b64encode(image_bytes).decode("utf-8")

# Prepare JSON payload
payload = {
    "filename": "image.png",
    "content_base64": encoded_image
}

# Convert to JSON string
json_payload = json.dumps(payload, indent=2)

print(json_payload[:200] + "...")  # Print a truncated version of the payload
```

> This is useful when you want to send the image data over an API in a text-based format like JSON.

---

### 🔹 Step 2: Decode and save the Base64 image back to file

```python
# Decode the base64 string back to bytes
decoded_image_bytes = base64.b64decode(payload["content_base64"])

# Write the decoded image to a new file
with open("restored_image.png", "wb") as f:
    f.write(decoded_image_bytes)
```

Now you’ll have a `restored_image.png` that is identical to the original `image.png`.

---

### ✅ This process works the same for PDFs:

Just replace `"image.png"` with `"document.pdf"` and `"rb"`/`"wb"` stays the same.

---



## ✅ Step-by-Step Example: Base64 File Upload with FastAPI

Here's how you can **upload a Base64-encoded file to a FastAPI backend**, and how the backend can **decode and save it as a real file**.


### 🔹 1. 📦 Client-Side (Python) – Encode & Send File as JSON

```python
import base64
import json
import requests

# Read file (e.g. PDF, image)
with open("document.pdf", "rb") as f:
    file_bytes = f.read()

# Encode as Base64
encoded_file = base64.b64encode(file_bytes).decode("utf-8")

# Prepare payload
payload = {
    "filename": "document.pdf",
    "content_base64": encoded_file
}

# Send POST request to FastAPI
response = requests.post("http://localhost:8000/upload-base64", json=payload)

print(response.status_code)
print(response.json())
```

---

### 🔹 2. 🚀 FastAPI Backend – Receive, Decode, and Save File

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
import os

app = FastAPI()

class Base64FileUpload(BaseModel):
    filename: str
    content_base64: str

@app.post("/upload-base64")
async def upload_base64_file(file: Base64FileUpload):
    try:
        # Decode Base64
        file_bytes = base64.b64decode(file.content_base64)
        
        # Save to disk
        output_path = os.path.join("uploaded_files", file.filename)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(file_bytes)

        return {"message": f"File '{file.filename}' saved successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

> When this endpoint is hit with a Base64-encoded file, FastAPI will decode and save it to `uploaded_files/document.pdf`.

---

### 🔐 Why use Base64 for file upload?

* Works well in environments where only text (like JSON) is accepted.
* Helpful in server-to-server or API-based file transfers.
* Avoids multipart form handling (simplifies API logic).

Would you like a version of this with a UI (e.g., using HTML + JavaScript)?
