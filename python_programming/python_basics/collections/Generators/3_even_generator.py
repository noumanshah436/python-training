def even_generator(max):
  n = 2

  while n <= max:
    yield n
    n += 2

for i in even_generator(10):
  print(i)
