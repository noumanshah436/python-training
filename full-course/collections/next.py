
### Simple Example of `next()` with a Condition

# we want to find an actor based on id

actors = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Charlie'}
]
 
# This give StopIteration error if actor is not found
actor = next(actor for actor in actors if actor['id'] == 2)

# next with default value, return default value if actor is not found
actor = next((actor for actor in actors if actor['id'] == 3), None)

# Output the result
print(actor)  # Output: {'id': 2, 'name': 'Bob'}

# ************************************************************



### Explanation
# 1. **Generator Expression**: `(actor for actor in actors if actor['id'] == actor_id_to_find)`
#    - This generator iterates through the `actors` list and yields each `actor` whose `'id'` matches `actor_id_to_find`.
   
# 2. **`next()` Function**:
#    - Retrieves the first item from the generator.
#    - If no item matches the condition, it returns `None`.
