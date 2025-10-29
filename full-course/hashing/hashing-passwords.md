To check if a **password used at login matches the one used at signup**, you **don’t store the original password** — instead, you:

---

### ✅ **At Signup:**

1. **Hash the password** (e.g., using SHA3-256 or `bcrypt`).
2. **Store the hash** in the database.

```python
import hashlib

password = "mySecret123"
password_hash = hashlib.sha3_256(password.encode()).hexdigest()

# Save `password_hash` in the database
```

---

### ✅ **At Login:**

1. Take the **password user entered**.
2. **Hash it** the same way.
3. Compare the **new hash** with the one stored in the database.

```python
login_password = "mySecret123"
login_hash = hashlib.sha3_256(login_password.encode()).hexdigest()

# Fetch stored_hash from database and compare
stored_hash = password_hash
if login_hash == stored_hash:
    print("✅ Password is correct")
else:
    print("❌ Invalid password")
```

---

### ⚠️ Why not store plain passwords?

Because if your database gets hacked, **users' actual passwords would be exposed**. Hashing them protects the data.

---

### 🔐 Use stronger hashing for passwords like `bcrypt`

SHA3-256 is fast (good for file integrity), but for passwords, **you want slow hashing** (to prevent brute force).

Example with `bcrypt`:

```python
import bcrypt

# Signup
password = b"mySecret123"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Store `hashed` in DB

# Login
entered_password = b"mySecret123"
if bcrypt.checkpw(entered_password, hashed):
    print("✅ Password match")
else:
    print("❌ Incorrect password")
```

Would you like me to help you implement this in your FastAPI project?
