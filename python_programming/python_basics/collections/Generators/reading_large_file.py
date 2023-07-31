def read_file(filename):
  f = open(filename, 'rt')

  for i in f:
    yield i
    
  f.close()



seq = read_file("large_file.txt")

# print(next(seq), end="")
# print(next(seq), end="")
# print(next(seq), end="")
# print(next(seq), end="")
for i in seq:
  print(i, end="")
