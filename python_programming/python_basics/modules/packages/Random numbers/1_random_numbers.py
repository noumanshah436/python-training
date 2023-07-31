import random

x = random.randint(1, 6)  # generate random int b/w 1 and 6 inclusive
y = random.random()  # generate random float b/w 0 and 1
x_ = random.random() * 100  # we can multiply it with any number( for 100 it generate 0 -100 numbers )

print(x)
print(y)

# ***************************************

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)
print(z)

# ***************************************

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]

random.shuffle(cards)

print(cards)
print(cards[3])


# ******************************************
#
# to install another module, type in terminal below

#  pip install module_name

# search it on google and explore its function
# no one can make this complete work for us
# we have to do it , ourself

