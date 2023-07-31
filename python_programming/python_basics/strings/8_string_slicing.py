# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]     =>  by default [0:endOfString:1]

#  +ve index =>  from left to right  "Nouman"   N=0 , o=1 , u=2 ...
#  -ve index =>  from right to left  "Nouman"   n=-1 , a=-2 , m=-3 , ...

name = "Bro Code"

first_name = name[:3]  # [0:3]  => [inclusive:exclusive]
last_name = name[4:]  # [4:8] => [4:end]
funky_name = name[::2]  # [0:8:2] => [0:end:2]  step is one by default
reversed_name = name[::-1]  # [0:8:-1] => [0:end:-1]

print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

sliced = slice(7, -4)

print(website1[sliced])
print(website2[sliced])

# *************************

website = "hello.com"
print(website[-4:])  # .com
a = website[-1:-5:-1]  # moc.
print(a[::-1])  # reverse a = .com
