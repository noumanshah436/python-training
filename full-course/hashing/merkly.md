The `merkly` Python package is typically used for **Merkle tree operations**, such as creating a Merkle root or verifying Merkle proofs. Merkle trees are cryptographic data structures used to verify the integrity of a collection of data efficiently and securely — without needing to compare every item.


The `merkly` Python package is used to **build Merkle Trees** and **generate/verify proofs** that a particular piece of data (like a file hash) exists in that tree. It’s a lightweight and easy way to work with **Merkle Trees** in Python.

---

### 🔍 Why use `merkly`?

You’d use `merkly` if you need to:

1. ✅ **Generate a Merkle root** from a list of hashes.
2. ✅ **Generate Merkle proofs** to prove that a specific item is part of a dataset.
3. ✅ **Verify Merkle proofs** without revealing the whole dataset.
4. ✅ **Reduce storage or bandwidth** by only transmitting the proof path instead of all data.

---

### 📦 Common use cases:

* **Blockchain** (Bitcoin, Ethereum): Merkle trees verify blocks of transactions.
* **Notarization services**: Prove a file was part of a notarized batch.
* **File verification**: Efficiently check integrity of large sets of data.

---

### 💡 Example using `merkly`

```python
from merkly import MerkleTree

# Some data hashes (e.g., file hashes)
hashes = [
    "a1b2c3...", "d4e5f6...", "789abc...", "def123..."
]

# Create Merkle Tree
tree = MerkleTree(hashes)

# Get the Merkle Root
print(tree.root)

# Generate a proof for the first item
proof = tree.get_proof(0)

# Verify the proof
valid = MerkleTree.verify_proof(hashes[0], proof, tree.root)
print("Valid proof?" , valid)
```

---

### 🧠 Summary

Use `merkly` if you’re building something that needs **proof of inclusion**, **batch verification**, or **blockchain-style data integrity**, like:

* Document notarization
* Secure file sharing
* Batch hashing systems

Would you like a real use case example (e.g., verifying uploaded files in a FastAPI app)?


### Merkle

A **Merkle** (short for **Merkle Tree**) is a **cryptographic data structure** used to efficiently and securely verify the contents of large datasets.

It was invented by **Ralph Merkle** and is widely used in **blockchains, secure data sharing, and file verification** systems.

---

### 🔗 Basic Idea

A **Merkle Tree** is a binary tree where:

* **Leaves** are hashes of data (e.g., files, transactions).
* **Each parent node** is the hash of its two child hashes.
* The **root node** (called the **Merkle Root**) summarizes the entire dataset.

---

### 📊 Visual Example

Imagine you have 4 files: `A`, `B`, `C`, and `D`.

1. First, hash each file:

   ```
   hA = hash(A)
   hB = hash(B)
   hC = hash(C)
   hD = hash(D)
   ```

2. Hash the pairs:

   ```
   hAB = hash(hA + hB)
   hCD = hash(hC + hD)
   ```

3. Finally, compute the Merkle Root:

   ```
   root = hash(hAB + hCD)
   ```

So the tree looks like this:

```
         root
        /    \
     hAB      hCD
    /  \     /   \
  hA   hB  hC   hD
```

---

### ✅ Why is it useful?

* **Efficient proof**: You can verify a single file without revealing all files.
* **Tamper detection**: Any change in data changes the Merkle Root.
* **Blockchain**: Bitcoin and Ethereum use Merkle Trees to verify transactions.

---

### 🧠 Real-world Analogy

Think of it like a **summary receipt** for a batch of files. If someone gives you that summary (Merkle Root), and a proof, you can verify whether your file was in the batch **without needing to see all the files**.

---

Would you like to see an example of how Merkle Trees are used in file notarization or smart contracts?


---

## 🔍 What is a Proof in Merkle Trees?

A **proof** is a set of **sibling hashes** that allows someone to verify that a particular value (like a file hash) is part of a Merkle Tree, **without knowing the full tree**.

Using the proof and the target hash, one can **recalculate the Merkle root**. If it matches the original root, then the data is valid and hasn’t been tampered with.

---

## 📦 `merkly` Package Overview

Install it:

```bash
pip install merkly
```

---

## ✅ Example Explained

```python
from merkly import MerkleTree

# Simulated file or data hashes (pretend you got them from files)
hashes = [
    "a1b2c3d4",  # Hash of file A
    "e5f6g7h8",  # Hash of file B
    "11223344",  # Hash of file C
    "55667788",  # Hash of file D
]

# Step 1: Create a Merkle Tree
tree = MerkleTree(hashes)

# Step 2: Print the Merkle Root (represents the whole tree/data)
print("Merkle Root:", tree.root)

# Step 3: Generate a proof that the first item (index 0) is in the tree
proof = tree.get_proof(0)

# Step 4: Verify that proof
is_valid = MerkleTree.verify_proof(hashes[0], proof, tree.root)
print("Is the proof valid?", is_valid)
```

---

## 🧠 What `get_proof(0)` Gives You

It returns the **sibling hashes** along the path from the data item to the root. For example:

```
         root
        /    \
     hAB      hCD
    /  \     /   \
  hA   hB  hC   hD
```

If you're verifying `hA`, your proof is:

* `hB` (sibling)
* `hCD` (uncle branch)

So you compute:

```python
step1 = hash(hA + hB)
step2 = hash(step1 + hCD) == root
```

---

## 📁 Why Use This in Real Life?

* **File Notarization**: Prove a file existed at a certain time.
* **Auditable Logs**: Verify log entries haven't been tampered with.
* **Blockchain**: Prove a transaction is part of a block.
* **Lightweight Clients**: Allow users to verify data without downloading everything.

---

Would you like a real-world file hash → Merkle tree → proof example in code using actual files?

