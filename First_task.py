# module imported to have the ability to use its functions (like randrange)
# for count = 0-100 (100 times) we define random number from 0 to 1000 and create a list

import random
how_many = 100

list_of_randoms = [random.randrange(0, 1000) for count in range(how_many)]

print(sorted(list_of_randoms))

# function declared to calculate avg value
# lists of even and odd numbers are created


def average(b):
    return sum(b) / len(b)


b = [a for a in list_of_randoms if a % 2 == 0]
c = [a for a in list_of_randoms if a % 2 != 0]

print(average(b))
print(average(c))
