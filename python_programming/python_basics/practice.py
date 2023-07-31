# List comprehension

ls = []
for i in range(100):
    if i%3==0:
        ls.append(i)

ls = [i for i in range(100) if i%3==0]

print(ls)
