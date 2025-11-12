


# A list of words
from collections import Counter


words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Create an empty Counter
word_count = Counter()

# Update it with the list
word_count.update(words)

# Print result
print(word_count.values())
