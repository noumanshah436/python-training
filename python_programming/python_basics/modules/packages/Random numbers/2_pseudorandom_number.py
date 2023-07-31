# The pseudorandom number generator is a mathematical function that generates a sequence of nearly random numbers.

# It takes a parameter to start off the sequence, called the seed.
# The function is deterministic, meaning given the same seed,
# it will produce the same sequence of numbers every time. The choice of seed does not matter.

# The seed() function will seed the pseudorandom number generator, taking an integer value as an argument,
# such as 1 or 7. If the seed() function is not called prior to using randomness, the default is to use the current system time in milliseconds from epoch (1970).

# The example below demonstrates seeding the pseudorandom number generator, generates some random numbers,
# and shows that reseeding the generator will result in the same sequence of numbers being generated.

# seed the pseudorandom number generator
from random import seed
from random import random
# seed random number generator
seed(1)
# generate some random numbers
print(random(), random(), random())
# reset the seed
seed(1)
# generate some random numbers
print(random(), random(), random())

# output
# 0.13436424411240122 0.8474337369372327 0.763774618976614
# 0.13436424411240122 0.8474337369372327 0.763774618976614
